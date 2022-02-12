import sys

from PyQt5.QtWidgets import (
    QApplication,
    QWidget
)
from PyQt5.QtCore import (
    QEasingCurve,
    QPoint,
    QPropertyAnimation, 
    QSequentialAnimationGroup,
    QSize,
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600,600)
        
        self.child = QWidget(self)
        self.child.setStyleSheet("background-color:red;border-radius:15px")
        self.child.resize(100,100)
        
        self.anim = QPropertyAnimation(self.child, b"pos")
        self.anim.setEndValue(QPoint(200,200))
        self.anim.setDuration(1500)

        self.anim_2 = QPropertyAnimation(self.child, b"size")
        self.anim_2.setEndValue(QSize(250,150))
        self.anim_2.setDuration(2000)

        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim)
        self.anim_group.addAnimation(self.anim_2)

        self.anim_group.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    app.exec()
