import os
import sys

from PyQt5 import QtWidgets, QtGui
import pyqtgraph as pg

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__()

        self.graph = pg.PlotWidget()

        self.setCentralWidget(self.graph)

        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,32,29,32,35,45]

        self.graph.setBackground('w')
        pen = pg.mkPen(color=(255,0,0))

        self.graph.plot(hour, temperature, pen=pen, symbol='+', symbolSize=30, symbolBrush=('b'))
        self.graph.setTitle("Your title here", color='b', size="30pt")
        styles = {'color':'red', 'font-size':'20px'}
        self.graph.setLabel('left', 'Temperature (°C)', **styles)
        self.graph.setLabel('bottom', 'Hour (H)', **styles)



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()


if __name__ == '__main__':
    main()


