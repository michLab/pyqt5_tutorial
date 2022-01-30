import os
import time
import sys

from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QDialog,
    QDialogButtonBox,
    QFileDialog,
    QLabel,
    QLineEdit,
    QMainWindow,
    QToolBar,
    QVBoxLayout,
)

from PyQt5.QtCore import QUrl, QSize, Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWebEngineWidgets import QWebEngineView


class HTMLData:
    def __init__(self):
        self._out_filename = "test.html"

    def get(self):
        return self._data

    def set_filename(self, fn):
        self._out_filename = fn

    def save_to_file(self, d):
        with open(self._out_filename, "w") as f:
            f.write(d)


class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("About Mozarella Ashbadger")

        QBtn = QDialogButtonBox.Ok
        self.button_box = QDialogButtonBox(QBtn)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        layout = QVBoxLayout()

        title = QLabel("Mozarella Ashbadger")
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)

        layout.addWidget(title)

        logo = QLabel()
        logo.setPixmap(QPixmap(os.path.join("icons", "ma-icon-128.png")))

        layout.addWidget(logo)

        layout.addWidget(QLabel("Version 23.35.211.233232"))
        layout.addWidget(QLabel("Copyright 2015 Mozarella Inc."))

        for i in range(layout.count()):
            layout.itemAt(i).setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.button_box)

        self.setLayout(layout)


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

        file_menu = self.menuBar().addMenu("&File")

        open_file_action = QAction(
            QIcon(os.path.join("images", "disk--arrow.png")), "Open file...", self
        )
        open_file_action.setStatusTip("Open from file")
        open_file_action.triggered.connect(self.open_file)
        file_menu.addAction(open_file_action)

        save_file_action = QAction(
            QIcon(os.path.join("images", "disk--pencil.png")), "Save page as...", self
        )
        save_file_action.setStatusTip("Save current page to file")
        save_file_action.triggered.connect(self.save_file)
        file_menu.addAction(save_file_action)

        help_menu = self.menuBar().addMenu("&Help")

        about_action = QAction(
            QIcon(os.path.join("icons", "question.png")),
            "About Mozarella Asgbadger",
            self,
        )
        about_action.setStatusTip("Find out more about Mozarella Ashbadger")
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)

        navigate_mozrella_action = QAction(
            QIcon(os.path.join("icons", "lifebuoy.png")),
            "Mozarella Ashbadger Homepage",
            self,
        )
        navigate_mozrella_action.setStatusTip("Go to Mozarella Ashbadger homepage")
        navigate_mozrella_action.triggered.connect(self.navigate_mozarella)
        help_menu.addAction(navigate_mozrella_action)

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

    def open_file(self):
        filename, _ = QFileDialog().getOpenFileName(
            self,
            "Open file",
            "",
            "Hypertext Markup Language (*.htm *html);;" "All files (*.*)",
        )

        if filename:
            with open(filename, "r") as f:
                html = f.read()

            self.browser.setHtml(html)
            self.url_bar.setText(filename)

    def save_file(self):
        filename, _ = QFileDialog().getSaveFileName(
            self,
            "Save page as",
            "",
            "Hypertext Markup Language (*.htm *html);;" "All files (*.*)",
        )

        if filename:
            html = HTMLData()
            html.set_filename(filename)
            test = self.browser.page().toHtml(html.save_to_file)

    def about(self):
        dlg = AboutDialog()
        dlg.exec()

    def navigate_mozarella(self):
        self.browser.setUrl(QUrl("https://www.pythonguis.com/courses/example-browser/"))


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
