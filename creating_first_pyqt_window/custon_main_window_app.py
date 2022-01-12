import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

# Subclass QMainWindow to customize your application's main window

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MyApp")
        button = QPushButton("Press me!")

        #self.setFixedSize(QSize(400, 300))
        self.setMinimumSize(QSize(200,100))
        self.setMaximumSize(QSize(400,200))

        # Set the central widget of the window
        self.setCentralWidget(button)


app = QApplication(sys.argv)

window = MainWindow()
window.show() 

app.exec()
