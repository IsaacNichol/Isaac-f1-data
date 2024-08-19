from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel,QLineEdit,QHBoxLayout
import sys
from elements import button_bootstrap_db
from elements import input

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
    #create horiztonal layout
    text_layout = QHBoxLayout()
    #create text field
    line_edit = QLineEdit()
    #create submit button
    submit_button = QPushButton('Submit')

    # Call the Bootstrap button function, passing `yes_button` as an argument
    submit_button.clicked.connect(lambda: input(submit_button,layout,line_edit))
    # Create text field to allow year entty
    text_layout.addWidget(line_edit) #TODO: Limit this field to only years
    #add submit button
    text_layout.addWidget(submit_button)
    # add horizontal layout
    layout.addLayout(text_layout)
    # Set the "layout" as the window layout

    window.setLayout(layout)

    # Show window to user
    window.show()

    # Run the application
    sys.exit(app.exec_())

bootstrap_box()
