import sys

from PyQt5.QtWidgets import (
    QApplication, QCheckBox, QComboBox,
    QDateEdit, QDateTimeEdit, QDial,
    QDoubleSpinBox, QFontComboBox, QLabel,
    QListWidget,
    QLCDNumber, QLineEdit, QMainWindow,
    QProgressBar, QPushButton, QRadioButton,
    QSlider, QSpinBox, QTimeEdit,
    QVBoxLayout, QWidget, QListWidgetItem
)
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QListWidget()
        widget.addItems(['One', 'Two', 'Three'])

        widget.currentItemChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    def index_changed(self, i:QListWidgetItem):
        print(i.text())

    def text_changed(self, s):
        print(s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
