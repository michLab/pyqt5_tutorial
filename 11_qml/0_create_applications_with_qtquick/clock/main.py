import os
import sys

from time import localtime, strftime

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QTimer, QObject, pyqtSignal

basedir = os.path.dirname(__file__)

app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load(os.path.join(basedir, 'main.qml'))

class Backend(QObject):

    updated = pyqtSignal(str, arguments=['time'])

    def __init__(self):
        super().__init__()
        self.timer = QTimer()
        self.timer.setInterval(100) # interval in ms
        self.timer.timeout.connect(self.update_time)
        self.timer.start()

    def update_time(self):    
        # Passs the current time to QML.
        curr_time = strftime("%H:%M:%S", localtime())
        self.updated.emit(curr_time)
        

# Define backend object poassed to QML.
backend = Backend()
engine.rootObjects()[0].setProperty('backend', backend)

backend.update_time()

sys.exit(app.exec())