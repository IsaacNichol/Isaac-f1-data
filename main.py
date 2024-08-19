from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel,QLineEdit,QHBoxLayout
from PyQt5.QtCore import QTimer
import sys
from data import database

def button_bootstrap_db(button):
    database.bootstrap_database()  # Call the function to bootstrap the database
    button.setText("Database Bootstrapped!") #TODO: add print out for when not applied

def bootstrap_box():
    app = QApplication(sys.argv)
    # Create the main window
    window = QWidget()
    window.setWindowTitle("F1 Data Downloader")

    # Create layout
    layout = QVBoxLayout()

    window.setGeometry(100, 100, 250, 100)

    # Create label for window
    text_header = [
        "Bootstrap the database?",
        "This creates all the needed schema on a pre-existing PostgreSQL database."
    ]

    # Loop over text headers
    for header in text_header:
        layout.addWidget(QLabel(header))

    # Create "Yes" button
    yes_button = QPushButton('Yes')

    # Call the Bootstrap button function, passing `yes_button` as an argument
    yes_button.clicked.connect(lambda: button_bootstrap_db(yes_button))

    # Add the button to the layout
    layout.addWidget(yes_button)

    session = "Please input year"
    layout.addWidget(QLabel(session))

    text_layout = QHBoxLayout()

    line_edit = QLineEdit()

    submit_button = QPushButton('Submit')

    text_layout.addWidget(line_edit) #TODO: Limit this field to only years
    text_layout.addWidget(submit_button)

    layout.addLayout(text_layout)
    # Set the "layout" as the window layout
    window.setLayout(layout)

    # Show window to user
    window.show()

    # Run the application
    sys.exit(app.exec_())

bootstrap_box()
