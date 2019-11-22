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
import platform
import traceback
from hashlib import sha1
from contextlib import contextmanager

INVALID_CHARCTER = """`~!@#$%^&*()+=_<>?/\|;"""

# OS helpers
isMac = sys.platform.startswith("darwin")
isWin = sys.platform.startswith("win32")
isLin = not isMac and not isWin

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