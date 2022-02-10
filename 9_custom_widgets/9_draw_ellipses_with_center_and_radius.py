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
        pen.setColor(QtGui.QColor(204, 0, 0))
        pen.setWidth(3)
        painter.setPen(pen)

        painter.drawEllipse(QtCore.QPoint(50, 50), 10, 10)
        painter.drawEllipse(QtCore.QPoint(50, 50), 15, 20)
        painter.drawEllipse(QtCore.QPoint(50, 50), 20, 30)
        painter.drawEllipse(QtCore.QPoint(50, 50), 25, 40)
        painter.drawEllipse(QtCore.QPoint(50, 50), 30, 50)
    
        painter.end()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
