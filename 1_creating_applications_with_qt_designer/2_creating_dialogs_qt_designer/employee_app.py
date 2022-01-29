import sys

from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QMainWindow,
    QPushButton,
)

from employer_dialog import Ui_Dialog

class EmployeeDlg(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Create instance of the GUI
        self.ui = Ui_Dialog()

        # Run setuUi() method to show the GUI
        self.ui.setupUi(self)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.centralWidget = QPushButton("Employee")
        self.centralWidget.clicked.connect(self.onEmployeeBtnClicked)

        self.setCentralWidget(self.centralWidget)

    def onEmployeeBtnClicked(self):
        dlg = EmployeeDlg(self)
        dlg.exec()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()

    sys.exit(app.exec())

