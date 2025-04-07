from CONSTANTS import Constants
from macros.toml_writer import TomlWriter

import ansi
import os

class Barrel:
    def __init__(self, name):
        self.name = name
        self.platform = "Windows 10"
        # ==========================
        self.user_home = os.getenv("HOME")
        self.user_path = os.getenv("PATH")
        self.user_path_split = self.user_path.split(":")
        # ==============================================
        self.common_directories = {
            "prefixes": os.path.join(self.user_home, ".local", "share", "barrels", "prefixes"),
            "barrel_storage": os.path.join(self.user_home, ".local", "share", "barrels", "storage")
        }

    '''
    Creates new barrel and returns two tuples of str and int.
        Str => Location of <name>.barrel.toml if not error
        Int => Success or failure
    '''
    def new(self) -> (str, int):
        probable_name = '-'.join(self.name.casefold().split(" "))
        barrel_file_name = f"{probable_name}.barrel.toml"

        print(f"{Constants.EMOJIS["info"]} Creating Barrel with the name of {barrel_file_name}")

        try:
            with open(os.path.join(self.common_directories["barrel_storage"], barrel_file_name), 'w') as barrel:
                toml = TomlWriter()

                barrel.write(toml.branch(barrel_file_name))
                barrel.write(toml.key_value("platform", self.platform))
                barrel.write(toml.key_value(
                    "path",
                    os.path.join(self.common_directories["barrel_storage"], barrel_file_name)
                    )
                )
        except Exception as e:
            print(f"{Constants.EMOJIS["critical"]} Couldn't create barrel! {e}")
            exit(1)
        finally:
            print(f"{Constants.EMOJIS["success"]} Created barrel {ansi.magenta(barrel_file_name)}!")
            print(f"Run {ansi.magenta(f"barrel init {barrel_file_name}")} to initialize everything.")

        return os.path.join(self.common_directories["barrel_storage"], barrel_file_name), 0

    '''
    Initializes barrel by parsing <barrel>.barrel.toml and creating a WINE/Proton prefix using it.
        Bool => True if succeeded, otherwise False.
    '''
    def init(self, barrel, setup_file="", proton_or_wine="") -> bool:
        (i, j) = (setup_file, proton_or_wine)

        if not setup_file:
            i = input("Please input the setup executable/direct executable you want the prefix to run: ")
        if not proton_or_wine:
            answered = False

            while not answered:
                k = input("Do you want to use Proton or WINE for the barrel [W/p/?]: ")

                match k.casefold():
                    case "w":
                        j = "WINE"
                        answered = True
                    case "p":
                        j = "Proton"
                        answered = True
                    case "?":
                        print("WINE   => Used for general purpose software like utilities found in Windows but not in Unix")
                        print("Proton => Valve's fork of WINE focused on gaming")
                    case _:
                        print("...")

        barrel_path = os.path.join(self.common_directories["barrel_storage"], barrel)

        if not os.path.isfile(barrel_path):
            print(f"{Constants.EMOJIS["critical"]} Cannot find barrel {ansi.magenta(barrel)}!")
            return False

        