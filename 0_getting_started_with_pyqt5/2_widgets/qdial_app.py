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

        widget = QDial()

        widget.setMinimum(-10)
        widget.setMaximum(100)
        # Or: widget.setRange(-10, 100)

        widget.setSingleStep(0.5)

        widget.valueChanged.connect(self.on_value_changed)
        widget.sliderMoved.connect(self.on_slider_moved)
        widget.sliderPressed.connect(self.on_slider_pressed)
        widget.sliderReleased.connect(self.on_slider_released)

        self.setCentralWidget(widget)

    def on_value_changed(self, i):
        print("Value: ", i)

    def on_slider_moved(self, p):
        print("Position: ", p)

    def on_slider_pressed(self):
        print("Pressed")

    def on_slider_released(self):
        print("Released")


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
