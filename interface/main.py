from interface.qt import *
from memento.utils import  isWin, isMac
import interface
from interface.form import main
from memento.controller import Controller

class MementoMainWindow(QMainWindow):
    def __init__(self, app, argv):
        QMainWindow.__init__(self)
        interface.main_window = self
        self.controller = Controller()
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
        self.form.button_add.clicked.connect(self.button_add_clicked)
        self.form.button_test.clicked.connect(self.button_test_clicked)
        self.form.button_browser.clicked.connect(self.button_browser_clicked)
        self.form.button_settings.clicked.connect(self.button_settings_clicked)

    def button_add_clicked(self):
        interface.dialog.open_dialog("add", self.controller)

    def button_test_clicked(self):
        interface.dialog.open_dialog("test", self.controller)

    def button_browser_clicked(self):
        interface.dialog.open_dialog("browser", self.controller)

    def button_settings_clicked(self):
        interface.dialog.open_dialog("settings", self.controller)

    
 

    