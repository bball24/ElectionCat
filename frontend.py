def load_settings():
    settings = {}
    with open("settings.cfg", "r") as settings_file:
        lines = settings_file.readlines()
        for line in lines:
            if line[0] == "#" or line == "\n" or line == "":
                continue
            key = line[:line.find("=")]
            value = line[line.find("=")+1:-1]
            settings[key] = value

    return settings


def check_admin_key(key, settings):
    if key == settings["admin_key"]:
        return True
    else:
        return False
