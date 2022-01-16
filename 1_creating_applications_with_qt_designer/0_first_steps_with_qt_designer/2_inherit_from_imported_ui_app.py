import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic

from mainwindow import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.label.setText("Filled in app")


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()