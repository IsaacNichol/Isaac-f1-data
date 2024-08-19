from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QCheckBox
import sys

app = QApplication(sys.argv)

# Create the main window
window = QWidget()
window.setWindowTitle("F1 Data Downloader")

# Create layout
layout = QVBoxLayout()

# Create the window
window.setLayout(layout)
window.show()

# Run the application
sys.exit(app.exec_())
