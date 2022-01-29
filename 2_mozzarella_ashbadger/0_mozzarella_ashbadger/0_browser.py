import sys

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
)

from PyQt5.QtCore import QUrl

from PyQt5.QtWebEngineWidgets import (
    QWebEngineView
)

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))

        self.setCentralWidget(self.browser)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
