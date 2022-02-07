import os
import sys
import time

from PyQt5 import QtWidgets, QtGui
import pyqtgraph as pg

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__()

        self.graph = pg.PlotWidget()

        self.setCentralWidget(self.graph)

        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature_1 = [30,32,34,32,33,32,29,32,35,45]
        temperature_2 = [50,35,44,22,38,32,27,38,32,44]


        # Set backgroudn color.
        self.graph.setBackground('w')
        # Add legend (must be before plot() is called?).
        self.graph.addLegend()
        # Set title.
        self.graph.setTitle("Your title here", color='b', size="30pt")
        # Set labels.
        styles = {'color':'red', 'font-size':'20px'}
        self.graph.setLabel('left', 'Temperature (°C)', **styles)
        self.graph.setLabel('bottom', 'Hour (H)', **styles)
        # Add grid.
        self.graph.showGrid(x=True, y=True)
        # Set range.
        self.graph.setXRange(0, 10, padding=0)
        self.graph.setYRange(20,50, padding=0)
        # Plot data.
        self.plot(x=hour, y=temperature_1, plotname='Sensor1', color='r')
        self.plot(x=hour, y=temperature_2, plotname='Sensor2', color='b', symbol='x')
        # Cleat the plot.
        time.sleep(5)
        self.graph.clear()
        
    def plot(self, x, y, plotname, color, symbol='+', symbolsize=30):
        pen = pg.mkPen(color=color)
        self.graph.plot(x, y, name=plotname, pen=pen, symbol=symbol, symbolSize=symbolsize, symbolBrush=(color))

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()


if __name__ == '__main__':
    main()


