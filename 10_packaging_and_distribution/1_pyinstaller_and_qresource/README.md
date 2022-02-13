# Based on
https://www.pythonguis.com/tutorials/packaging-data-files-pyqt5-with-qresource-system/

# Build app with qresources
```console
pyinstaller 0_app.py 
```
# Open QtDesigner on Ubuntu:
1. Install QtDesigner
```console
sudo apt-get install qt5-designer
```
2. Run QtDesigner
```console
designer
```

# Compiling the UI file
```console
pyuic5 mainwindow.ui -o MainWindow.py
```

# Compiling the resources file
```console
pyrcc5 resources.qrc -o resources_rc.py
```