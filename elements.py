from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel,QLineEdit,QHBoxLayout
from data import database
from urllib.request import urlopen
import json
import psycopg2
import api
import sys
def button_bootstrap_db(button):
    database.bootstrap_database()  # Call the function to bootstrap the database
    button.setText("Database Bootstrapped!")  # TODO: add print out for when not applied


def input(button, layout, line_edit):  # todo: only allow 1 press #TODO: add handeling when year return error EG 2028
    year = line_edit.text()
    session_url = "https://api.openf1.org/v1/sessions?year=" + year + "&session_type=Race&session_name=Race"
    response = urlopen(session_url)
    session_data = json.loads(response.read().decode('utf-8'))
    circuit_name = [item["circuit_short_name"] for item in session_data]

    for sessions in circuit_name:
        layout.addWidget(QLabel(sessions))

    race(button, layout, line_edit)


def race(button, layout, line_edit,circuit_name):
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
    submit_button.clicked.connect() #TODO: Call API > DB Here


