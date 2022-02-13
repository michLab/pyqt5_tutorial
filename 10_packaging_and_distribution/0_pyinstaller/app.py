import os
import sys

from PyQt5 import QtWidgets, QtGui

basedir = os.path.dirname(__file__) 

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
        layout = QtWidgets.QVBoxLayout()

        label = QtWidgets.QLabel("My simple app")
        label.setMargin(10)
        layout.addWidget(label)

        button = QtWidgets.QPushButton("Push")
        button.setIcon(QtGui.QIcon(os.path.join(basedir, 'icons', 'tick.png')))
        button.pressed.connect(self.close)
        layout.addWidget(button)

        container = QtWidgets.QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(os.path.join(basedir, 'icons', 'animal-dog.png')))
    window = MainWindow()
    app.exec()