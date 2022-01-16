import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()

        self.button_is_checked = True

        self.setWindowTitle("My App")

        self.button = QPushButton("Click me!")
        self.button.setCheckable(True)
        self.button.setChecked(self.button_is_checked)
        self.button.released.connect(self.the_button_was_released)
        
        self.setCentralWidget(self.button)


    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()

        print(self.button_is_checked)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()