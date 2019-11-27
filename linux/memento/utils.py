import os
import sys
import json

INVALID_CHARCTER = """`~!@#$%^&*()+=_<>?/\|;[]{},."""

DEFAULT_CONFIG = """{"field": 0, "test": 1, "hint": 1, "num": 10}"""

# OS helpers
isMac = sys.platform.startswith("darwin")
isWin = sys.platform.startswith("win32")
isLin = not isMac and not isWin
base_folder = None

def format_string(string):
    result = string.strip().lower()
    if result == "":
        return result
    w = []
    
    for i in range(len(result)-1):
        if result[i] == " " and result[i+1] == " ":
            continue
        w.append(result[i])

    w.append(result[-1])
    result = "".join(w)
    return result

def is_invalid_string(string):
    for char in string:
        if char in INVALID_CHARCTER:
            return False
    return True

def load_config():
        global base_folder
        file = os.path.join(base_folder, "config.json")
        if os.path.exists(file) == False:
            with open(file, "w") as config_file:
                config_file.write(DEFAULT_CONFIG) 
        with open(file, "r") as config_file:
            config = json.load(config_file)
        config_file.close()
        return config

def save_config(config):
        global base_folder
        file = os.path.join(base_folder, "config.json")

        with open(file, "w") as config_file:
            json.dump(config, config_file)
        config_file.close()

def set_base_folder():
    global base_folder
    if isWin:
        from memento.winpaths import get_appdata
         
        base_folder = os.path.join(get_appdata(), "Memento")
        return base_folder
    else:
        dataDir = os.path.expanduser("~/.local/share/Memento")
        if not os.path.exists(dataDir):
            os.makedirs(dataDir)
        base_folder = dataDir
        return base_folder


