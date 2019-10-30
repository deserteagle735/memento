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

# some add-ons expect json to be in the utils module
import json # pylint: disable=unused-import

# used in ankiweb
def base62(num, extra=""):
    s = string; table = s.ascii_letters + s.digits + extra
    buf = ""
    while num:
        num, i = divmod(num, len(table))
        buf = table[i] + buf
    return buf

_base91_extra_chars = "!#$%&()*+,-./:;<=>?@[]^_`{|}~"
def base91(num):
    # all printable characters minus quotes, backslash and separators
    return base62(num, _base91_extra_chars)

def guid64():
    "Return a base91-encoded 64bit random number."
    return base91(random.randint(0, 2**64-1))

# increment a guid by one, for note type conflicts
def incGuid(guid):
    return _incGuid(guid[::-1])[::-1]

def _incGuid(guid):
    s = string; table = s.ascii_letters + s.digits + _base91_extra_chars
    idx = table.index(guid[0])
    if idx + 1 == len(table):
        # overflow
        guid = table[0] + _incGuid(guid[1:])
    else:
        guid = table[idx+1] + guid[1:]
    return guid

# Fields
##############################################################################

def joinFields(list):
    return "\x1f".join(list)

def splitFields(string):
    return string.split("\x1f")

# Checksums
##############################################################################

def checksum(data):
    if isinstance(data, str):
        data = data.encode("utf-8")
    return sha1(data).hexdigest()

def fieldChecksum(data):
    # 32 bit unsigned number from first 8 digits of sha1 hash
    return int(checksum(stripHTMLMedia(data).encode("utf-8"))[:8], 16)

# Temp files
##############################################################################

_tmpdir = None

def tmpdir():
    "A reusable temp folder which we clean out on each program invocation."
    global _tmpdir
    if not _tmpdir:
        def cleanup():
            shutil.rmtree(_tmpdir)
        import atexit
        atexit.register(cleanup)
        _tmpdir = os.path.join(tempfile.gettempdir(), "anki_temp")
    if not os.path.exists(_tmpdir):
        os.mkdir(_tmpdir)
    return _tmpdir

def tmpfile(prefix="", suffix=""):
    (fd, name) = tempfile.mkstemp(dir=tmpdir(), prefix=prefix, suffix=suffix)
    os.close(fd)
    return name

def namedtmp(name, rm=True):
    "Return tmpdir+name. Deletes any existing file."
    path = os.path.join(tmpdir(), name)
    if rm:
        try:
            os.unlink(path)
        except (OSError, IOError):
            pass
    return path

# Cmd invocation
##############################################################################

@contextmanager
def noBundledLibs():
    oldlpath = os.environ.pop("LD_LIBRARY_PATH", None)
    yield
    if oldlpath is not None:
        os.environ["LD_LIBRARY_PATH"] = oldlpath

def call(argv, wait=True, **kwargs):
    "Execute a command. If WAIT, return exit code."
    # ensure we don't open a separate window for forking process on windows
    if isWin:
        si = subprocess.STARTUPINFO()
        try:
            si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        except:
            # pylint: disable=no-member
            si.dwFlags |= subprocess._subprocess.STARTF_USESHOWWINDOW
    else:
        si = None
    # run
    try:
        with noBundledLibs():
            o = subprocess.Popen(argv, startupinfo=si, **kwargs)
    except OSError:
        # command not found
        return -1
    # wait for command to finish
    if wait:
        while 1:
            try:
                ret = o.wait()
            except OSError:
                # interrupted system call
                continue
            break
    else:
        ret = 0
    return ret

# OS helpers
##############################################################################

isMac = sys.platform.startswith("darwin")
isWin = sys.platform.startswith("win32")
isLin = not isMac and not isWin
devMode = os.getenv("ANKIDEV", "")

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