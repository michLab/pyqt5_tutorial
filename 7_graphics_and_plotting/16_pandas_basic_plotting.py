import os
import sys

import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

import pandas as pd

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__()

        # Create the matplotlib FigureCanvas object,
        # which defines a single set of axes as self.axes
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        
        # Create pandas DataFrae with some simple data and headers.
        df = pd.DataFrame(
            [[0,10], [5,15], [2,20], [15,25], [4,10]],
            columns=['A', 'B']
        )

        # Plot the pendas DataFrame, passing in the matplotlib Canvas axes.
        df.plot(ax=sc.axes)
        
        self.setCentralWidget(sc)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()


if __name__ == '__main__':
    main()


