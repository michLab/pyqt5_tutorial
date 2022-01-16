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
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        # widget = QLabel("Hello")
        # font = widget.font()
        # font.setPointSize(30)
        # widget.setFont(font)
        # widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        widget = QLabel()
        pixmap = QPixmap('lena.png')
        widget.setPixmap(pixmap)
        widget.setScaledContents(True)
        
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
