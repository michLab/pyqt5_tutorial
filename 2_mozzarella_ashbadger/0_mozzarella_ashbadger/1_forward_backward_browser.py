import os
import sys

from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QToolBar,
)
from PyQt5.QtCore import QUrl, QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWebEngineWidgets import QWebEngineView


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.browser = QWebEngineView()
        self.home_url = "https://www.google.com"
        self.browser.setUrl(QUrl(self.home_url))
        self.browser.urlChanged.connect(self.update_url_bar)
        self.browser.loadFinished.connect(self.update_title)

        self.setCentralWidget(self.browser)
        self.setWindowTitle("Mozarella Ashbedger")

        nav_tb = QToolBar("Navigation")
        nav_tb.setIconSize(QSize(16, 16))
        self.addToolBar(nav_tb)

        back_btn = QAction(QIcon(os.path.join("images", "arrow-180.png")), "Back", self)
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect(self.browser.back)
        nav_tb.addAction(back_btn)

        next_btn = QAction(
            QIcon(os.path.join("images", "arrow-000.png")), "Forward", self
        )
        next_btn.setStatusTip("Forward to next page")
        next_btn.triggered.connect(self.browser.forward)
        nav_tb.addAction(next_btn)

        reload_btn = QAction(
            QIcon(os.path.join("images", "arrow-circle-315.png")), "Reload", self
        )
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect(self.browser.reload)
        nav_tb.addAction(reload_btn)

        home_btn = QAction(QIcon(os.path.join("images", "home.png")), "Home", self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(self.navigate_home)
        nav_tb.addAction(home_btn)

        self.https_icon = QLabel()
        self.https_icon.setPixmap(QPixmap(os.path.join("images", "lock-nossl.png")))
        nav_tb.addWidget(self.https_icon)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        nav_tb.addWidget(self.url_bar)

        stop_btn = QAction(
            QIcon(os.path.join("images", "cross-circle.png")), "Stop", self
        )
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(self.browser.stop)
        nav_tb.addAction(stop_btn)

    def update_url_bar(self, url):
        if url.scheme == "https":
            self.https_icon.setPixmap(QPixmap(os.path.join("images", "lock-ssl.png")))
        else:
            self.https_icon.setPixmap(QPixmap(os.path.join("images", "lock-nossl.png")))

    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("%s - Mozarella Ashbedger" % title)

    def navigate_home(self):
        self.browser.setUrl(QUrl(self.home_url))

    def navigate_to_url(self):
        url = QUrl(self.url_bar.text())

        if url.scheme() == "":
            url.setScheme("http")
        self.browser.setUrl(url)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
