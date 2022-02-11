import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

COLORS = [
# 17 undertones https://lospec.com/palette-list/17undertones
'#000000', '#141923', '#414168', '#3a7fa7', '#35e3e3', '#8fd970', '#5ebb49',
'#458352', '#dcd37b', '#fffee5', '#ffd035', '#cc9245', '#a15c3e', '#a42f3b',
'#f45b7a', '#c24998', '#81588d', '#bcb0c2', '#ffffff',
]

class Canvas(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
    
        pixmap = QtGui.QPixmap(400, 300)
        self.setPixmap(pixmap)

        self._last_x = None
        self._last_y = None

        self.pen_color = QtGui.QColor('#000000')

    def set_pen_color(self, c):
        self.pen_color = QtGui.QColor(c)

    def mouseMoveEvent(self, a0: QtGui.QMouseEvent):
        if self._last_x is None:
            self._last_x = a0.x()
            self._last_y = a0.y()

        painter = QtGui.QPainter(self.pixmap())

        pen = QtGui.QPen()
        pen.setColor(self.pen_color)
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

class QPalleteButton(QtWidgets.QPushButton):
    def __init__(self, color):
        super().__init__()
        self.setFixedSize(QtCore.QSize(24, 24))
        self.color = color
        self.setStyleSheet("background-color: %s;" % color)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.canvas = Canvas()

        w = QtWidgets.QWidget()
        l = QtWidgets.QVBoxLayout()
        w.setLayout(l)
        l.addWidget(self.canvas)

        palette = QtWidgets.QHBoxLayout()
        self.add_palette_buttons(palette)
        l.addLayout(palette)

        self.setCentralWidget(w)

    def add_palette_buttons(self, layout):
        for c in COLORS:
            b = QPalleteButton(c)
            b.pressed.connect(lambda c=c: self.canvas.set_pen_color(c))
            layout.addWidget(b)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
