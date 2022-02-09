import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QPainter, QPen
from PyQt5.QtWidgets import (
    QApplication,
    QGraphicsEllipseItem,
    QGraphicsItem,
    QGraphicsRectItem,
    QGraphicsScene,
    QGraphicsView,
    QHBoxLayout,
    QPushButton,
    QSlider,
    QVBoxLayout,
    QWidget,
)


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Define a scene rect of 400x200, with it's origin at 0,0
        # If we don't set this on creation, we can set it later with .setSceneRect()
        self.scene = QGraphicsScene(0, 0, 400, 200)

        # Draw rectalngle item, setting dimension.
        rect = QGraphicsRectItem(0, 0, 200, 50)

        # Set the origin (position) of the rectangle in the scene.
        rect.setPos(50, 20)

        # Define the brush (fill).
        brush = QBrush(Qt.red)
        rect.setBrush(brush)

        # Define the pen (line).
        pen = QPen(Qt.cyan)
        pen.setWidth(10)
        rect.setPen(pen)

        # Draw circle item, setting dimension.
        ellipse = QGraphicsEllipseItem(0, 0, 100, 100)

        # Set the origin (position) of the ellipse in the scene.
        ellipse.setPos(75, 30)

        # Define the brush (fill).
        brush = QBrush(Qt.blue)
        ellipse.setBrush(brush)

        # Define the pen (line).
        pen = QPen(Qt.green)
        pen.setWidth(10)
        ellipse.setPen(pen)

        # Add item to the scene. Items are stacked in the order they are added.
        self.scene.addItem(ellipse)
        self.scene.addItem(rect)

        # Set all items to be movable.
        for item in self.scene.items():
            item.setFlag(QGraphicsItem.ItemIsMovable)
            item.setFlag(QGraphicsItem.ItemIsSelectable)

        # Define the layout.
        vbox = QVBoxLayout()

        up = QPushButton("Up")
        up.clicked.connect(self.up)
        vbox.addWidget(up)

        down = QPushButton("Down")
        down.clicked.connect(self.down)
        vbox.addWidget(down)

        rotate = QSlider()
        rotate.setRange(0,360)
        rotate.valueChanged.connect(self.rotate)
        vbox.addWidget(rotate)

        view = QGraphicsView(self.scene)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox)
        hbox.addWidget(view)

        self.setLayout(hbox)

    def up(self):
        '''
        Iterate all selected items moving them forward.
        '''
        items = self.scene.selectedItems()
        for item in items:
            z = item.zValue()
            item.setZValue(z + 1)

    def down(self):
        '''
        Iterate all selected items moving them backward.
        '''
        items = self.scene.selectedItems()
        for item in items:
            z = item.zValue()
            item.setZValue(z - 1)

    def rotate(self, value):
        '''
        Iterate all selected items rotating them.
        '''
        items = self.scene.selectedItems()
        for item in items:
            item.setRotation(value)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    app.exec()
    