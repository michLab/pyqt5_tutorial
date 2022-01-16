import sys

from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QMainWindow,
    QMessageBox,
    QPushButton,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)

        self.setCentralWidget(button)

    def button_clicked(self, s):
        button = QMessageBox.critical(
            self,
            "Oh dear!",
            "Something went very wrong",
            buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore,
            defaultButton=QMessageBox.Discard)

        if button == QMessageBox.Discard:
            print("Discard!")
        elif button==QMessageBox.NoToAll:
            print("No to all!")
        else:
            print("Ignore!")


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
