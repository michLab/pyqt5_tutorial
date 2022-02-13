from ast import arguments
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

    hms = pyqtSignal(int, int, int, arguments=['hours', 'minutes', 'seconds'])

    def __init__(self):
        super().__init__()
        self.timer = QTimer()
        self.timer.setInterval(100) # interval in ms
        self.timer.timeout.connect(self.update_time)
        self.timer.start()

    def update_time(self):    
        # Pass the current time to QML.
        time = localtime()
        self.hms.emit(time.tm_hour, time.tm_min, time.tm_sec)
        

# Define backend object poassed to QML.
backend = Backend()
engine.rootObjects()[0].setProperty('backend', backend)

backend.update_time()

sys.exit(app.exec())