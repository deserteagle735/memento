import os
from memento import utils
from memento.db import DB

class Controller(object):
    
    def __init__(self):
        self.base_folder = utils.set_base_folder()
        self.database_path = os.path.join(self.base_folder, "database.db")
        self.first_run = False
        self.check_meta()
        self.db = DB(self.database_path, first_run= self.first_run)

    def check_meta(self):
        """
        Check if database created or not
        """
        if not os.path.exists(self.database_path):
            self.first_run = True
        self.media_folder_path = os.path.join(self.base_folder, "media")
        if not os.path.exists(self.media_folder_path):
            os.makedirs(self.media_folder_path)

        

            
    
        

    