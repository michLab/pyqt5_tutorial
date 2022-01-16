from PyQt5.QtWidgets import QApplication, QWidget

# Access the comman line arguments
import sys

# We need only one QApplication instance per application.
# You can pass command line arguments to it:
app = QApplication(sys.argv)

# Create QWidget which will be our window:
window = QWidget()
window.show() # windows are hidden by default

# Start the event loop
app.exec()

# The appliaction won't reach here until you exit and the event loop
# has stopped