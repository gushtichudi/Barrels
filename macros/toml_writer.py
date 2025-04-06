class TomlWriter:
    def __init__(self):
        pass

    def branch(self, name: str):
        return f"[{name}]"

    def key_value(self, key: str, value: str):
        return f"{key} = {value}"

# For testing purposes
# ====================
#
# if __name__ == '__main__':
#    toml = TomlWriter()
#
#    print(toml.branch("half-life-2"))
#    print(toml.key_value("platform", "Windows 10"))
#    print(toml.key_value("path", "/home/foo/.local/share/barrels/prefixes/half-life-2"))