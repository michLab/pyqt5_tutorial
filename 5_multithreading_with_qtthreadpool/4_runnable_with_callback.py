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

    Inherits from QRunnable to handle worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function
    '''

    def __init__(self, fn, *args, **kwargs):
        super().__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):
        self.fn(*self.args, **self.kwargs)

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

    def execute_this_fn(self):
        print("Hello!")

    def oh_no(self):
        worker = Worker(self.execute_this_fn)
        self.threadpool.start(worker)

    def recurring_timer(self):
        self.counter += 1
        self.l.setText(f"Counter: {self.counter}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()