import sys

from PyQt5.QtWidgets import (
    QApplication, QCheckBox, QComboBox,
    QDateEdit, QDateTimeEdit, QDial,
    QDoubleSpinBox, QFontComboBox, QLabel,
    QLCDNumber, QLineEdit, QMainWindow,
    QProgressBar, QPushButton, QRadioButton,
    QSlider, QSpinBox, QTimeEdit,
    QVBoxLayout, QWidget,
)
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QComboBox()
        widget.addItems(['One', 'Two', 'Three'])
        widget.setEditable(True)
        widget.setInsertPolicy(QComboBox.InsertAlphabetically)
        widget.setMaxCount(5)

        # Send the current position of the selscted item.
        widget.currentIndexChanged.connect(self.index_changed)

        # There is an alternate signal to send the current text.
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    def index_changed(self, i: int):
        print("Index: %d" % i)

    def text_changed(self, s):
        print("Text: %s" % s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
