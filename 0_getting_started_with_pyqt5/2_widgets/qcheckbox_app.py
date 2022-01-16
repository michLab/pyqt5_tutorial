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

        widget = QCheckBox()
        widget.setCheckState(Qt.Checked)
        widget.setTristate(True)

        widget.stateChanged.connect(self.show_state)

        self.setCentralWidget(widget)
    
    def show_state(self, s):
        print(s == Qt.Checked)
        print(s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
