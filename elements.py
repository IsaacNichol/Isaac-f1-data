from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel,QLineEdit,QHBoxLayout
from PyQt5.QtWidgets import QComboBox
from data import database
from urllib.request import urlopen
import json
import psycopg2
import api
import sys


def bootstrap_ui(layout):
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


def button_bootstrap_db(button):
    database.bootstrap_database()  # Call the function to bootstrap the database
    button.setText("Database Bootstrapped!")  # TODO: add print out for when not applied


def user_input_ui(layout):
    session = "Please input year"
    layout.addWidget(QLabel(session))
    # create horiztonal layout
    text_layout = QHBoxLayout()
    # create text field
    line_edit = QLineEdit()
    # create submit button
    submit_button = QPushButton('Submit')
    # Call the Bootstrap button function, passing `yes_button` as an argument
    submit_button.clicked.connect(lambda: race_selector(submit_button, layout, line_edit))
    # Create text field to allow year entty
    text_layout.addWidget(line_edit)  # TODO: Limit this field to only years
    # add submit button
    text_layout.addWidget(submit_button)
    # add horizontal layout
    layout.addLayout(text_layout)
    # Set the "layout" as the window layout


def error_parsing_url(layout,e):
    layout.addWidget(QLabel(f"{e}"))


def race_selector(button, layout, line_edit):  # todo: only allow 1 press #TODO: add handeling when year return error EG 2028
    comboBox = QComboBox()
    year = line_edit.text()
    try:
        session_url = "https://api.openf1.org/v1/sessions?year="+year+"&session_type=Race&session_name=Race"
        response = urlopen(session_url)
        session_data = json.loads(response.read().decode('utf-8'))
        circuit_name = [item["circuit_short_name"] for item in session_data]
        for sessions in circuit_name:
            comboBox.addItem(sessions)

        layout.addWidget(comboBox)
        race_input(button, layout, circuit_name)
    except Exception as e:
            error_parsing_url(layout,e)


def race_input(button, layout,circuit_name):
    session = "Please input race"

    layout.addWidget(QLabel(session))
    # create horiztonal layout
    text_layout = QHBoxLayout()
    # create text field
    line_edit = QLineEdit()
    # create submit button
    submit_button = QPushButton('Submit')

    # Create text field to allow year entty
    text_layout.addWidget(line_edit)  # TODO: Limit this field to only races in list
    # add submit button
    text_layout.addWidget(submit_button)
    # add horizontal layout
    layout.addLayout(text_layout)
    # Set the "layout" as the window layout

    # Call the Bootstrap button function, passing `yes_button` as an argument
    #submit_button.clicked.connect() #TODO: Call API > DB Here


