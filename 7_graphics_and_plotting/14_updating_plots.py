import os
from random import randint
import sys

import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


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
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.setCentralWidget(self.canvas)

        # Generate data.
        n_data = 50
        self.xdata = list(range(n_data))
        self.ydata = [randint(0,10) for i in range(n_data)]
        self.update_plot()

        # Set a timer to trigger the redraw by calling update_plot
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self):
        # Drop off the first element, append new one.
        self.ydata = self.ydata[1:] + [randint(0,10)]
        self.canvas.axes.cla() # Clear the canvas.
        self.canvas.axes.plot(self.xdata, self.ydata, 'r')
        # Trigger the canvas to update and redraw.
        self.canvas.draw()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()


if __name__ == '__main__':
    main()


