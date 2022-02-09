import sys

from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # Define a scene rect of 400x200, with it's origin at 0,0
    # If we don't set this on creation, we can set it later with .setSceneRect()
    scene = QtWidgets.QGraphicsScene(0, 0, 400, 200)

    # Draw rectalngle item, setting dimension.
    rect = QtWidgets.QGraphicsRectItem(0, 0, 200, 50)

    # Set the origin (position) of the rectangle in the scene.
    rect.setPos(50, 20)

    # Define the brush (fill).
    brush = QtGui.QBrush(QtCore.Qt.red)
    rect.setBrush(brush)

    # Define the pen (line).
    pen = QtGui.QPen(QtCore.Qt.cyan)
    pen.setWidth(10)
    rect.setPen(pen)

    # Draw circle item, setting dimension.
    ellipse = QtWidgets.QGraphicsEllipseItem(0, 0, 100, 100)

    # Set the origin (position) of the ellipse in the scene.
    ellipse.setPos(75, 30)

    # Define the brush (fill).
    brush = QtGui.QBrush(QtCore.Qt.blue)
    ellipse.setBrush(brush)

    # Define the pen (line).
    pen = QtGui.QPen(QtCore.Qt.green)
    pen.setWidth(10)
    ellipse.setPen(pen)

    # Move along Z-axis.
    ellipse.setZValue(500)
    rect.setZValue(200)
    # ellipse.stackAfter(rect)

    # Add item to the scene. Items are stacked in the order they are added.
    scene.addItem(ellipse)
    scene.addItem(rect)

    view = QtWidgets.QGraphicsView(scene)
    view.show()

    app.exec()