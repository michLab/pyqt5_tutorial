import resource
import sys

from PyQt5 import QtGui, QtWidgets

import resources

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Hello App")

        self.button = QtWidgets.QPushButton("Click me")

        icon = QtGui.QIcon(":/icons/penguin.png")
        self.button.setIcon(icon)
        self.button.clicked.connect(self.change_icon)

        self.setCentralWidget(self.button)

    def change_icon(self):
        icon = QtGui.QIcon(":/icons/monkey.png")
        self.button.setIcon(icon)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
