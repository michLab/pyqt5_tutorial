from PyQt5 import QtWidgets, QtGui, QtCore, uic

import sys
from resources.MainWindow import Ui_MainWindow

try:
    # Include in try/except block if you're also targeting Mac/Linux
    from ctypes import windll  # Only exists on Windows.
    myappid = 'mycompany.myproduct.subproduct.version'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Load the UI
        self.setupUi(self)

        # Set value of counter
        self.counter = 0
        self.update_counter()

        # Bind
        self.btn_inc.clicked.connect(self.inc)
        self.btn_dec.clicked.connect(self.dec)
        self.btn_reset.clicked.connect(self.reset)
    
    def update_counter(self):
        self.label.setText(str(self.counter))

    def inc(self):
        self.counter += 1
        self.update_counter()

    def dec(self):
        self.counter -= 1
        self.update_counter()

    def reset(self):
        self.counter = 0
        self.update_counter()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(':/icons/counter.ico'))
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
 