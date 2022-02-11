import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
    
        self._last_x = None
        self._last_y = None

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 300)
        self.label.setPixmap(canvas)

        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, a0: QtGui.QMouseEvent):
        if self._last_x is None:
            self._last_x = a0.x()
            self._last_y = a0.y()

        painter = QtGui.QPainter(self.label.pixmap())

        pen = QtGui.QPen()
        pen.setColor(QtGui.QColor('green'))
        pen.setWidth(3)
        painter.setPen(pen)

        painter.drawLine(self._last_x, self._last_y, a0.x(), a0.y())
        painter.end()
        self.update()

        self._last_x = a0.x()
        self._last_y = a0.y()

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent):
        self._last_x = None
        self._last_y = None

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
