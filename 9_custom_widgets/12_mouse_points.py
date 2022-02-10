import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 300)
        self.label.setPixmap(canvas)

        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, a0: QtGui.QMouseEvent):
        painter = QtGui.QPainter(self.label.pixmap())

        pen = QtGui.QPen()
        pen.setColor(QtGui.QColor('green'))
        pen.setWidth(3)
        painter.setPen(pen)

        painter.drawPoint(a0.x(), a0.y())
        painter.end()
        self.update()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
