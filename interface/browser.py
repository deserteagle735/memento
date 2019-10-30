import interface
from interface.qt import *

class Browser(QDialog):
    def __init__(self):
        QDialog.__init__(self, None, Qt.Window)
        self.setModal(True)
        self.setup_ui() 
        
    def setup_ui(self):
        self.setup_dialog()
        self.show()

    def setup_dialog(self):
        # main window
        from interface.form import browser
        self.form = interface.form.browser.Ui_Dialog()
        self.form.setupUi(self)

    
        
    
        