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

        widget = QSpinBox()
        #widget = QDoubleSpinBox()

        widget.setMinimum(-10)
        widget.setMaximum(3)
        # Or: widget.setRange(-10, 3)

        widget.setPrefix('$')
        widget.setSuffix('c')
        widget.setSingleStep(3)
        widget.valueChanged.connect(self.on_value_changed)

        self.setCentralWidget(widget)

    def on_value_changed(self, i):
        print(i)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
