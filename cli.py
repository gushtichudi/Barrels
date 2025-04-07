from cmds import handler
from CONSTANTS import Constants
from jobs import checks

import os
import platform
import pwd
import sys

import ansi
from cmds.handler import Handler

class Cli:
    def __init__(self, prompt):
        self.prompt = prompt
        self.emojis = {
            "info": "ℹ️",
            "success": "✅",
            "warning": "⚠️",
            "error": "❌",
            "critical": "‼️",
            "undefined_exception": "⁉️",
            "question": "❓",
            "star": "✴️"
        }
        # ===================
        self.username = ansi.magenta(pwd.getpwuid(os.getuid())[0])
        self.os = ansi.magenta(sys.platform)
        self.arch = ansi.magenta(platform.machine())
        # ===================
        self.VERSION = Constants.VERSION

    def greeting(self):
        print(f"{self.emojis["star"]} Hello, {self.username}! This is Barrels {self.VERSION} running on an {self.arch} in {self.os}")
        print(f"{self.emojis["info"]} Type {ansi.magenta("`help`")} for a list of commands to start working with.")
        term_col = os.get_terminal_size().columns

        print(f"{ansi.gray("-")}" * term_col)

    def field(self):
        status = True

        while status:
            x = input(f"{self.prompt} ")

            # print(f"{self.emojis["info"]} Command line response: {x}")
            hnd = handler.Handler(x)
            hnd.start()

    def start(self):
        chk = checks.Checks()
        chk.start()

        self.greeting()
        self.field()