from CONSTANTS import Constants
import macros.file_or_dir_creations as fdc

import os

class Checks:
    def __init__(self):
        # also used in barrel.py
        self.user_home = os.getenv("HOME")
        self.user_path = os.getenv("PATH")
        self.user_path_split = self.user_path.split(":")
        # ==============================================
        self.common_directories = {
            "prefixes": os.path.join(self.user_home, ".local", "share", "barrels", "prefixes"),
            "barrel_storage": os.path.join(self.user_home, ".local", "share", "barrels", "storage")
        }

    def check_for_files(self) -> int:
        if not fdc.dir_exists(self.common_directories["prefixes"]):
            return 1
        elif not fdc.dir_exists(self.common_directories["barrel_storage"]):
            return 2
        else:
            return 0

    def start(self):
        match self.check_for_files():
            case 0:
                pass
            case 1:
                print(f"{Constants.EMOJIS["critical"]} General Barrel directories cannot be found!")
                print("Trying to create it ourselves...")

                try:
                    os.makedirs(self.common_directories["prefixes"], exist_ok=True)
                except Exception as e:
                    print(f"{Constants.EMOJIS["critical"]} An error occurred! {e}")

                print(f"{Constants.EMOJIS["info"]} Try again.")
            case 2:
                print(f"{Constants.EMOJIS["critical"]} General Barrel directories cannot be found!")
                print("Trying to create it ourselves...")

                try:
                    os.makedirs(self.common_directories["barrel_storage"], exist_ok=True)
                except Exception as e:
                    print(f"{Constants.EMOJIS["critical"]} An error occurred! {e}")