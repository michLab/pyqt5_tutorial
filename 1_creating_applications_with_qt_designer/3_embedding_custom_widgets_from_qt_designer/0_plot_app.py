import os
import sys

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow
)

from pyqtgraph import PlotWidget, plot

from PyQt5 import uic


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Load the UI Page
        uic.loadUi('mainwindow.ui', self)

        self.plot([1,2,3,4], [5,6,7,8])

        self.setCentralWidget(self.graphWidget)

    def plot(self, x, y):
        self.graphWidget.plot(x, y)


def main():
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()

