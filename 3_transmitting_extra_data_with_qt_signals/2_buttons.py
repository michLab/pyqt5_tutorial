import sys 

from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)

        v = QVBoxLayout()
        h = QHBoxLayout()

        for a in range(10):
            button = QPushButton(str(a))
            button.pressed.connect(
                lambda val=a: self.button_pressed(val)
            )
            h.addWidget(button)
        
        v.addLayout(h)
        self.label = QLabel("")
        v.addWidget(self.label)
        
        self.setLayout(v)

    def button_pressed(self, n):
        self.label.setText(str(n))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()       