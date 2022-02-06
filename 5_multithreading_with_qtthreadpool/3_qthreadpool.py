import sys
import time

from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from PyQt5.QtCore import (
    QRunnable,
    QTimer,
    QThreadPool,
    pyqtSlot,
)


class Worker(QRunnable):
    '''
    Worker thread
    '''

    @pyqtSlot()
    def run(self):
        '''
        Your code goes to this function
        '''
        print("Thread start")
        time.sleep(5)
        print("Thread complete")

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.counter = 0

        self.threadpool = QThreadPool()
        print(f"Multithreading with maximum {self.threadpool.maxThreadCount()} threads.") 

        layout = QVBoxLayout()

        self.l = QLabel("Start")
        b = QPushButton("DANGER!")
        b.pressed.connect(self.oh_no)

        layout.addWidget(self.l)
        layout.addWidget(b)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)
        self.show()

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

    def oh_no(self):
        worker = Worker()
        self.threadpool.start(worker)

    def recurring_timer(self):
        self.counter += 1
        self.l.setText(f"Counter: {self.counter}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()