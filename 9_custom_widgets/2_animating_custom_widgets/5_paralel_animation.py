import sys

from PyQt5.QtWidgets import (
    QApplication,
    QGraphicsOpacityEffect,
    QWidget
)
from PyQt5.QtCore import (
    QEasingCurve,
    QPoint,
    QPropertyAnimation, 
    QParallelAnimationGroup,
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

        effect = QGraphicsOpacityEffect(self.child)
        self.child.setGraphicsEffect(effect)
        self.anim_2 = QPropertyAnimation(effect, b"opacity")
        self.anim_2.setStartValue(0)
        self.anim_2.setEndValue(1)
        self.anim_2.setDuration(2000)

        self.anim_group = QParallelAnimationGroup()
        self.anim_group.addAnimation(self.anim)
        self.anim_group.addAnimation(self.anim_2)

        self.anim_group.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    app.exec()
