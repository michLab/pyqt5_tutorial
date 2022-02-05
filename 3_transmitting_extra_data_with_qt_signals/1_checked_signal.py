import sys 

from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QMainWindow
)

from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    
    def __init__(self, parent=None):
        super().__init__(parent)

        checkbox = QCheckBox("Checked?")

        # Option 1: conversion function
        def checkstate_to_bool(state):
            if state == Qt.Checked:
                return self.result(True)
            return self.result(False)

        checkbox.stateChanged.connect(checkstate_to_bool)

        # Option 2: Dictionary lookup:
        _convert = {
            Qt.Checked: True,
            Qt.Unchecked: False
        }

        checkbox.stateChanged.connect(lambda x: self.result(_convert[x]))

        self.setCentralWidget(checkbox)

    # SLOT: Accepts the check value:
    def result(self, v):
        print(v)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()       