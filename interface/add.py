import interface
from interface.qt import *

class Add(QDialog):
    def __init__(self):
        QDialog.__init__(self, None, Qt.Window)
        self.setModal(True)
        self.setup_ui() 
        
    def setup_ui(self):
        self.setup_dialog()
        self.show()

    def setup_dialog(self):
        # main window
        from interface.form import add
        self.form = interface.form.add.Ui_Dialog()
        self.form.setupUi(self)

    
        
    
        