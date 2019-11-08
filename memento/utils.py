import re
import os
import random
import time
import math
from html.entities import name2codepoint
import subprocess
import tempfile
import shutil
import string
import sys
import locale
from hashlib import sha1
import platform
import traceback
from contextlib import contextmanager

# OS helpers
isMac = sys.platform.startswith("darwin")
isWin = sys.platform.startswith("win32")
isLin = not isMac and not isWin
invalidFilenameChars = ":*?\"<>|"

def invalidFilename(str, dirsep=True):
    for c in invalidFilenameChars:
        if c in str:
            return c
    if (dirsep or isWin) and "/" in str:
        return "/"
    elif (dirsep or not isWin) and "\\" in str:
        return "\\"
    elif str.strip().startswith("."):
        return "."