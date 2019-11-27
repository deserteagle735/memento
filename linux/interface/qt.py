import os
import sys

from memento.utils import isWin, isMac

from PyQt5.Qt import *
# trigger explicit message in case of missing libraries
# instead of silently failing to import
try:
    from PyQt5 import sip
except ImportError:
    import sip

from PyQt5.QtCore import pyqtRemoveInputHook # pylint: disable=no-name-in-module
from PyQt5.QtCore import *
from PyQt5 import QtCore

qtmajor = (QT_VERSION & 0xff0000) >> 16
qtminor = (QT_VERSION & 0x00ff00) >> 8
qtpoint = QT_VERSION & 0xff

if qtmajor != 5 or qtminor < 9 or qtminor == 10:
    raise Exception("Memento does not support your Qt version.")

# GUI code assumes python 3.6+
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    raise Exception("Memento requires Python 3.6+")
