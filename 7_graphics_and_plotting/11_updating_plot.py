import os
import sys
import time

from random import randint

from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__()

        self.graph = pg.PlotWidget()

        self.setCentralWidget(self.graph)

        # Generate data
        self.x = list(range(100)) # 100 point of time
        self.y = [randint(0,100) for _ in range(100)] # 100 data points

        # Set background color.
        self.graph.setBackground('w')
      
        pen = pg.mkPen(color=(255,0,0))
        self.data_line = self.graph.plot(self.x, self.y, pen=pen)

        # Create timer to change data.
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):
        self.x = self.x[1:] # Remove first element
        self.x.append(self.x[-1] + 1) # Add new value 1 higher than the last

        self.y = self.y[1:] # Remove first element
        self.y.append(randint(0,100)) # Add new random value

        self.data_line.setData(self.x, self.y)
        


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()


if __name__ == '__main__':
    main()


