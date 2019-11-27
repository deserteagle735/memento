import sys

if sys.version_info[0] < 3 or sys.version_info[1] < 5:
    raise Exception("Memento requires Python 3.5+")

if sys.getfilesystemencoding().lower() in ("ascii", "ansi_x3.4-1968"):
    raise Exception("<Memento requires a UTF-8 locale.")

version="1.0"