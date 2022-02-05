import sys

from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QColorDialog,
    QMenu,
    QSystemTrayIcon,
)

from PyQt5.QtGui import (
    QIcon,
)

app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)

# Create the icon
icon = QIcon("animal-dog.png")

clipboard = QApplication.clipboard()
dialog = QColorDialog()

def copy_color_rgb():
    if dialog.exec():
        color = dialog.currentColor()
        clipboard.setText(f"rgb({color.red()}, {color.green()}, {color.blue()})")

def copy_color_hex():
    if dialog.exec():
        color = dialog.currentColor()
        clipboard.setText(color.name())

def copy_color_hsv():
    if dialog.exec():
        color = dialog.currentColor()
        clipboard.setText(f"hsv({color.hue()}, {color.saturation()}, {color.value()})")


# Create the tray
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

# Create the menu
menu = QMenu()

action1 = QAction("Hex")
action1.triggered.connect(copy_color_hex)
menu.addAction(action1)

action2 = QAction("RGB")
action2.triggered.connect(copy_color_rgb)
menu.addAction(action2)

action3 = QAction("HSV")
action3.triggered.connect(copy_color_hsv)
menu.addAction(action3)

quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

# Add the menu to the tray
tray.setContextMenu(menu)

app.exec()
