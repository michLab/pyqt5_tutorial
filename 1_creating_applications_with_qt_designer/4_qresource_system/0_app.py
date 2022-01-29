import sys

from PyQt5 import QtGui, QtWidgets

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Hello App")

        self.button = QtWidgets.QPushButton("Click me")

        icon = QtGui.QIcon("animal-penguin.png")
        self.button.setIcon(icon)
        self.button.clicked.connect(self.change_icon)

        self.setCentralWidget(self.button)

    def change_icon(self):
        icon = QtGui.QIcon("animal-monkey.png")
        self.button.setIcon(icon)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
