import sys

from PyQt5 import QtWidgets


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # Define a scene rect of 400x200, with it's origin at 0,0
    # If we don't set this on creation, we can set it later with .setSceneRect()
    scene = QtWidgets.QGraphicsScene(0, 0, 400, 200)

    view = QtWidgets.QGraphicsView(scene)
    view.show()

    app.exec()