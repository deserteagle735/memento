import traceback
import sys
from interface.qt import *
import interface

def run():
    try:
        _run()
    except Exception as e:
        traceback.print_exc()
        QMessageBox.critical(None, "Startup Error",
                             "Please notify support of this error:\n\n"+
                             traceback.format_exc())

def _run():
    QCoreApplication.setApplicationName("Memento")
    app = MementoApplication(sys.argv)
    import interface.main
    main_window = interface.main.MementoMainWindow(app, sys.argv)

    app.exec_()

class MementoApplication(QApplication):

    def __init__(self, argv):
        QApplication.__init__(self, argv)
        self._argv = argv
       

class DialogManager():
    def __init__(self):
        self.dialog_function = {
            "add" : self.add,
            "browser": self.browser
        }

    def open_dialog(self, dialog_name, controller):
        self.dialog_function[dialog_name](controller)

    def add(self, controller):
        import interface.add
        self.dialog_add = interface.add.Add(controller)

    def browser(self, controller):
        import interface.browser
        self.dialog_browser = interface.browser.Browser(controller)

dialog = DialogManager()
