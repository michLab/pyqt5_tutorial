import sys

from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # Get the raw value.
            value = self._data[index.row()][index.column()]

            # Perform per-type checks and render accordingly.
            if (isinstance(value, datetime)):
                # Render time to YYYY-MM-DD:
                return value.strftime("%Y-%m-%d")
            elif isinstance(value, float):
                # Render float to 2 dp:
                return f"{value:.2f}"
            else:
                return value
    
    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])

    
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        data = [
            [4, 9, 2],
            [1, -1, 'hello'],
            [3.023, 5, -5],
            [3, 3, datetime(2017,10,1)],
            [7.555, 8, 9],
        ]

        self.model = TableModel(data)

        self.table = QtWidgets.QTableView()
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()


    