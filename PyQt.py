from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton,QHBoxLayout
import sys

app = QApplication(sys.argv)

# Create the main window
window = QWidget()
window.setWindowTitle("F1 Data Downloader")

# Create layout
layout = QVBoxLayout()

# Create label for window

text_header = ["Bootstrap the database?",
        "This creates all the needed schema on a pre-existing postgres database."]
for header in text_header:
    layout.addWidget(QLabel(header))

# Create a horizontal layout for the buttons
button_layout = QHBoxLayout()

# Add "Yes" and "No" buttons to the horizontal layout
button_layout.addWidget(QPushButton('Yes'))
button_layout.addWidget(QPushButton('No'))

# Add the horizontal layout with buttons to the main layout
layout.addLayout(button_layout)

# Create the window
window.setLayout(layout)
window.show()

# Run the application
sys.exit(app.exec_())
