import sys

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QPlainTextEdit,
    QVBoxLayout,
    QWidget,
)

from PyQt5.QtCore import QProcess

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.btn = QPushButton("Execute")
        self.btn.pressed.connect(self.start_process)

        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)

        l = QVBoxLayout()
        l.addWidget(self.btn)
        l.addWidget(self.text)

        w = QWidget()
        w.setLayout(l)

        self.setCentralWidget(w)

    def message(self, s):
        self.text.appendPlainText(s)

    def start_process(self):
        self.message("Executing process.")
        self.p = QProcess()
        self.p.start("python3", ['dummy_script.py'])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()

    app.exec()