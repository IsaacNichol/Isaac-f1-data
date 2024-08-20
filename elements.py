from PyQt5.QtWidgets import QPushButton, QLabel,QLineEdit,QHBoxLayout
from PyQt5.QtWidgets import QComboBox
from data import database
from urllib.request import urlopen
from process import requested
import json


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
    year = "Please input year"
    layout.addWidget(QLabel(year))
    # create horiztonal layout
    text_layout = QHBoxLayout()
    # create text field
    line_edit = QLineEdit()
    # create submit button
    submit_button = QPushButton('Submit') #TODO: Hitting this mutiple times shows multiple slectoin boxes. Ishould be removing the old and creating a new
    # Call the Bootstrap button function, passing `yes_button` as an argument
    submit_button.clicked.connect(lambda: track_selector(submit_button, layout, line_edit))
    # Create text field to allow year entty
    text_layout.addWidget(line_edit)  # TODO: Limit this field to only years
    # add submit button
    text_layout.addWidget(submit_button)
    # add horizontal layout
    layout.addLayout(text_layout)
    # Set the "layout" as the window layout


def error_parsing_url(layout,e):
    layout.addWidget(QLabel(f"{e}"))


def track_selector(button, layout, line_edit):  # todo: only allow 1 press #TODO: add handeling when year return error EG 2028
    track_comboBox = QComboBox()
    year = line_edit.text()
    try:
        session_url = "https://api.openf1.org/v1/sessions?year="+year+"&session_type=Race&session_name=Race"
        response = urlopen(session_url)
        session_data = json.loads(response.read().decode('utf-8'))
        circuit_name = [item["circuit_short_name"] for item in session_data]
        track_comboBox.addItem("")
        for sessions in circuit_name:
            track_comboBox.addItem(sessions)
        layout.addWidget(track_comboBox)
        track_input(button, layout, circuit_name,track_comboBox,year)
    except Exception as e:
            error_parsing_url(layout,e)


def track_input(button, layout,circuit_name,track_comboBox,year):

    current_selected = QLabel(track_comboBox.currentText())

    def on_combobox_changed(index):
        current_selected.setText(track_comboBox.currentText())
        #print(f'{comboBox.currentText()} is requested')
    # Connect the combo box selection change event to the function
    track_comboBox.currentIndexChanged.connect(on_combobox_changed)

    selection = "Race selected"
    layout.addWidget(QLabel(selection))

    # create horiztonal layout
    selection_layout = QHBoxLayout()

    selection_button = QPushButton('Confirm race request')
    # create text field

    selection_layout.addWidget(current_selected)
    # add submit button
    selection_layout.addWidget(selection_button)
    # add horizontal layout
    layout.addLayout(selection_layout)

    def on_selection(index):
        selection_button.setHidden(True)
        selected_track = track_comboBox.currentText()
        session_selector(circuit_name,layout,button,year,selected_track)

    selection_button.clicked.connect(on_selection)


def session_selector(circuit_name,layout,button,year,selected_track):  # todo: only allow 1 press #TODO: add handeling when year return error EG 2028
    session = "Please select session"
    layout.addWidget(QLabel(session))
    comboBox = QComboBox()
    print("https://api.openf1.org/v1/sessions?year="+year+"&circuit_short_name="+selected_track)
    try:
        session_url = "https://api.openf1.org/v1/sessions?year="+year+"&circuit_short_name="+selected_track
        response = urlopen(session_url)
        session_data = json.loads(response.read().decode('utf-8'))
        session_name = [item["session_name"] for item in session_data]
        comboBox.addItem("")
        for sessions in session_name:
            comboBox.addItem(sessions)
        layout.addWidget(comboBox)
        session_input(button, layout,selected_track,comboBox)
    except Exception as e:
            error_parsing_url(layout,e)


def session_input(button, layout,selected_track,comboBox):

    current_selected = QLabel(comboBox.currentText())

    def on_combobox_changed(index):
        current_selected.setText(comboBox.currentText())
        #print(f'{comboBox.currentText()} is requested')
    # Connect the combo box selection change event to the function
    comboBox.currentIndexChanged.connect(on_combobox_changed)

    selection = "Race selected"
    layout.addWidget(QLabel(selection))

    # create horiztonal layout
    selection_layout = QHBoxLayout()

    selection_button = QPushButton('Confirm race request')
    # create text field

    selection_layout.addWidget(current_selected)
    # add submit button
    selection_layout.addWidget(selection_button)
    # add horizontal layout
    layout.addLayout(selection_layout)

    def on_selection(index):
        session_type = comboBox.currentText()
        requested(selected_track,session_type)
        selection_button.setHidden(True)

    selection_button.clicked.connect(on_selection)


