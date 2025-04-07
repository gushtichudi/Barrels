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