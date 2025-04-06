# TODO: add more escapes

def bold(s):
    return f"\x1b[1m{s}\x1b[0m"

def magenta(s):
    return f"\x1b[35m{s}\x1b[0m"

def gray(s):
    return f"\u001B[1m\u001B[90m{s}\u001B[39m\u001B[22m"