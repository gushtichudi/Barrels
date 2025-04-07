from art import text2art

import ansi
from CONSTANTS import Constants
from cmds.barrel import Barrel


class Handler:
    def __init__(self, command_line):
        self.command_line = command_line
        self.argv = self.command_line.split(" ")

    def parse_cmd(self):
        ### ZERO
        match self.argv[0]:
            case "ls":
                print("TODO: ls")
            case "about":
                print(text2art("Barrels"))
                print()
                print(f"Version: {Constants.VERSION}")
                print(f"Last encounter with `&#86;`: {ansi.magenta("Apr 6 2025")}")
                print(f"Developer net worth: {ansi.magenta("17.35 United States Dollar")}")
            case "exit":
                exit(0)
            case "barrel":
                ### ONE
                if len(self.argv) <= 1:
                    print(f"{Constants.EMOJIS["error"]} {ansi.magenta(self.argv[0])} needs more parameters!")
                    print(f"Usage: {ansi.magenta(self.argv[0])} [new | show | del | init <barrel>]")
                else:
                    ### TWO
                    # print("TODO: barrel")
                    if len(self.argv) <= 2:
                        print(f"{Constants.EMOJIS["error"]} {ansi.magenta(self.argv[1])} needs more parameters!")
                        print(f"Usage: {ansi.magenta(self.argv[0])} [new | show | del | init <barrel>]")
                    else:
                        ### THREE
                        prefix_name = self.argv[2]
                        input(f"Press enter if this is the correct name: {prefix_name}")

                        barrel = Barrel(prefix_name)

                        match self.argv[1]:
                            case "new":
                                barrel.new()
                            case _:
                                print("todo")
            case _:
                print(f"{Constants.EMOJIS["error"]} {ansi.magenta(self.argv[0])} is not a valid command!")
        print()

    def start(self):
        self.parse_cmd()