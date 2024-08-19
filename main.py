from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel,QLineEdit,QHBoxLayout
import sys
from elements import bootstrap_ui
from elements import user_input_ui

# Initialise Qt
app = QApplication(sys.argv)
# Create the main window
window = QWidget()
# Set the window size
window.setWindowTitle("F1 Data Downloader")
# Create layout
layout = QVBoxLayout()
# set size of window
window.setGeometry(100, 100, 250, 100)
# Call elements that make up bootstrap UI
bootstrap_ui(layout)
# Call elements that make up Sessions & Race user input
user_input_ui(layout)
# Confrim layout as per design
window.setLayout(layout)
# Show window to user
window.show()
# Run the application
sys.exit(app.exec_())


