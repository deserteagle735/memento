from interface.qt import *
from memento.utils import  isWin, isMac
import interface
from interface.form import main
from interface.add import Add
import traceback

class MementoMainWindow(QMainWindow):
    def __init__(self, app, argv):
        QMainWindow.__init__(self)
        interface.main_window = self
        self.setup_ui()   

    def setup_ui(self):
        self.setup_main_window()
        self.setup_button()
        self.show()

    # Main window setup
    ##########################################################################

    def setup_main_window(self):
        # main window
        self.form = interface.form.main.Ui_MainWindow()
        self.form.setupUi(self)
    
    def setup_button(self):
        self.form.button_add.clicked.connect(self.on_button_add_clicked)
        self.form.button_browser.clicked.connect(self.on_button_browser_clicked)

    def on_button_add_clicked(self):
        interface.dialog.open_dialog("add")

    def on_button_browser_clicked(self):
        interface.dialog.open_dialog("browser")
    
 

    