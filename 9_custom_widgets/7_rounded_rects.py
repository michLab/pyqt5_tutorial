import sys
from random import randint, choice

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt

colors = ["#FFD141", "#376F9F", "#0D1F2D", "#E9EBEF", "#EB5160"]


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 300)
        self.label.setPixmap(canvas)

        self.setCentralWidget(self.label)

        self.draw_something()

    def draw_something(self):
        painter = QtGui.QPainter(self.label.pixmap())
        
        pen = QtGui.QPen()
        pen.setColor(QtCore.Qt.green)
        pen.setWidth(3)
        painter.setPen(pen)

        brush = QtGui.QBrush()
        brush.setColor(QtGui.QColor('#FFD141'))
        brush.setStyle(Qt.Dense1Pattern)
        painter.setBrush(brush)
    
        painter.drawRoundedRect(50, 50, 100, 100, 10, 10)
        painter.drawRoundedRect(60, 60, 150, 100, 10, 50)
        painter.drawRoundedRect(70, 70, 100, 150, 50, 10)
        painter.drawRoundedRect(80, 80, 150, 100, 30, 20)
        painter.drawRoundedRect(90, 90, 100, 150, 100, 200)
    
        painter.end()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
