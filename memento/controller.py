from memento.utils import isWin, isLin
from memento.db import DB
import os

class Controller(object):
    
    def __init__(self):
        self.base_folder = self.set_base_folder()
        self.database_path = os.path.join(self.base_folder, "database.db")
        self.first_run = False
        self.check_meta()
        self.db = DB(self.database_path, first_run= self.first_run)
        

    def set_base_folder(self):
        if isWin:
            from memento.winpaths import get_appdata
            return os.path.join(get_appdata(), "Memento")
        else:
            dataDir = os.path.expanduser("~/.local/share/Memento")
            if not os.path.exists(dataDir):
                os.makedirs(dataDir)
            return dataDir

    def check_meta(self):
        """
        Check if database created or not
        """
        if not os.path.exists(self.database_path):
            self.first_run = True
        self.media_folder_path = os.path.join(self.base_folder, "media")
        if not os.path.exists(self.media_folder_path):
            os.makedirs(self.media_folder_path)


        

            
    
        

    