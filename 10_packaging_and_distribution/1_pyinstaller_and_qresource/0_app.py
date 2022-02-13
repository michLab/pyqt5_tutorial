import os
import sys
import resources

from PyQt5 import QtWidgets, QtGui

try:
    from ctypes import windll  # Only exists on Windows.
    myappid = 'mycompany.myproduct.subproduct.version'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Hello world")

        label = QtWidgets.QLabel("My simple app")
        label.setMargin(10)

        self.setCentralWidget(label)

        self.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(":/icons/animal-dog.png"))
    window = MainWindow()
    app.exec()



