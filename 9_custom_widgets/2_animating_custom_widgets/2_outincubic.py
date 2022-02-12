import sys

from PyQt5.QtWidgets import (
    QApplication,
    QWidget
)
from PyQt5.QtCore import QPropertyAnimation, QPoint, QEasingCurve

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600,600)
        
        self.child = QWidget(self)
        self.child.setStyleSheet("background-color:red;border-radius:15px")
        self.child.resize(100,100)
        
        self.anim = QPropertyAnimation(self.child, b"pos")
        self.anim.setEasingCurve(QEasingCurve.OutInCubic)
        self.anim.setEndValue(QPoint(400,400))
        self.anim.setDuration(1500)
        self.anim.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    app.exec()
