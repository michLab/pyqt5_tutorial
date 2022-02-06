import sys

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QPlainTextEdit,
    QVBoxLayout,
    QWidget,
)

from PyQt5.QtCore import QProcess


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.p = None

        self.btn = QPushButton("Execute")
        self.btn.pressed.connect(self.start_process)

        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)

        l = QVBoxLayout()
        l.addWidget(self.btn)
        l.addWidget(self.text)

        w = QWidget()
        w.setLayout(l)

        self.setCentralWidget(w)

    def message(self, s):
        self.text.appendPlainText(s)

    def start_process(self):
        if self.p is None:
            self.message("Executing process.")
            self.p = QProcess()
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)
            self.p.start("python3", ["7_dummy_script.py"])

    def handle_stdout(self):
        data = self.p.readAllStandardOutput()
        stdout = bytes(data).decode('utf-8')
        self.message(stdout)

    def handle_stderr(self):
        data = self.p.readAllStandardError()
        stderr = bytes(data).decode('utf-8')
        self.message(stderr)

    def handle_state(self, state):
        states = {
            QProcess.NotRunning: "Not running",
            QProcess.Starting: "Starting",
            QProcess.Running: "Running",
        }
        state_name = states[state]
        self.message(f"State changed: {state_name}")

    def process_finished(self):
        self.message("Process finished")
        self.p = None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()

    app.exec()
