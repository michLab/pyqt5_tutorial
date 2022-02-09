import sys

from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # Define a scene rect of 400x200, with it's origin at 0,0
    # If we don't set this on creation, we can set it later with .setSceneRect()
    scene = QtWidgets.QGraphicsScene(0, 0, 400, 200)

    rectitem = QtWidgets.QGraphicsRectItem(0, 0, 360, 20)
    rectitem.setPos(20, 20)
    rectitem.setBrush(QtGui.QBrush(QtCore.Qt.red))
    rectitem.setPen(QtGui.QPen(QtCore.Qt.cyan))
    scene.addItem(rectitem)

    textitem = scene.addText("QGraphics is fun!")
    textitem.setPos(100, 200)

    scene.addPolygon(
        QtGui.QPolygonF(
            [
                QtCore.QPointF(30, 60),
                QtCore.QPointF(270, 40),
                QtCore.QPointF(400, 200),
                QtCore.QPointF(20, 150),
            ]
        ),
            QtGui.QPen(QtCore.Qt.darkGreen)
    )

    pixmap = QtGui.QPixmap("lena.png")
    pixmapitem = scene.addPixmap(pixmap)
    pixmapitem.setPos(250, 70)


    view = QtWidgets.QGraphicsView(scene)
    view.setRenderHint(QtGui.QPainter.Antialiasing)
    view.show()

    app.exec()