from urllib.request import urlopen
import json
import pandas as pd


base = 'https://api.openf1.org/v1/'
methods = [
    'sessions?',
    'car_data?',
    'drivers?',
    'intervals?',
    'laps?',
    'location?',
    'meetings?',
    'pit?',
    'position?',
    'race control?',
    'stints?',
    'team radio?',
    'weather?'
]
variables = [
    'year=',
    'driver_number=',
    'session_key=',
    'country_name='
]
year = '2023'
and_session = '&'+variables[2]+'9197'
session = variables[2]+'9197'


session_url = base + methods[0] + variables[0] + year+and_session
response = urlopen(session_url)
session_data = json.loads(response.read().decode('utf-8'))
session_keys = [item["session_key"] for item in session_data]
country_code = [item["country_code"] for item in session_data]
session_type = [item["session_type"] for item in session_data]

combined_data_session = list(zip(session_keys, country_code,session_type))

print(combined_data_session)

driver_url = base + methods[2]+session
response = urlopen(driver_url)
driver_data = json.loads(response.read().decode('utf-8'))
broadcast_name = [item["broadcast_name"] for item in driver_data]
driver_number = [item["driver_number"] for item in driver_data]
session_key_driver = [item["session_key"] for item in driver_data]
team_name = [item["team_name"] for item in driver_data]

combined_data_driver = list(zip(broFixes adcast_name,driver_number,session_key_driver,team_name))

print(combined_data_driver)

#Position data

position_url = base + methods[8]+session
response = urlopen(position_url)
position_data = json.loads(response.read().decode('utf-8'))
driver_number_position = [item["driver_number"] for item in position_data]
session_key_position = [item["session_key"] for item in position_data]
position = [item["position"] for item in position_data]
date = [item["date"] for item in position_data]

combined_data_position = list(zip(driver_number_position,session_key_position,position,date))
print(combined_data_position)
