from CONSTANTS import Constants
import macros.file_or_dir_creations as fdc

import ansi
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
            "barrel_storage": os.path.join(self.user_home, ".local", "share", "barrels", "storage"),
            "runner_dir": os.path.join(self.user_home, ".local", "share", "barrels", "runners")
        }

    def check_for_files(self) -> int:
        for directory in self.common_directories:
            if not fdc.dir_exists(self.common_directories[directory]):
                print(f"{Constants.EMOJIS["error"]} Crucial directory {ansi.magenta(directory)} can't be found!")
                print(f"Creating directory {ansi.magenta(directory)}...")

                try:
                    os.makedirs(self.common_directories[directory], exist_ok=True)
                except Exception as e:
                    print(f"{Constants.EMOJIS["critical"]} {ansi.magenta(e)}")
                else:
                    return 1
                finally:
                    return 0

        print()
        return 1


    def start(self):
        if 0 is not self.check_for_files():
            print(f"{Constants.EMOJIS["critical"]} Not possible...")