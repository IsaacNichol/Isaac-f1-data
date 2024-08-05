from urllib.request import urlopen
import json
import pandas as pd
import psycopg2
conn = psycopg2.connect(
    dbname="postgres",
    user="",
    password="",
    host="local.host",
    port="5432"
)

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

# Fetching session data
url = base + methods[0] + variables[0] + year
response = urlopen(url)
data = json.loads(response.read().decode('utf-8'))
print(data)
session_keys = [item["session_key"] for item in data]

# Extracting session keys
#session_keys = [item["session_key"] for item in data]

#for key in session_keys:
#    result_url = base + methods[2] + variables[2] + str(key)
#    print(result_url)

#    try:
#         response_2 = urlopen(result_url)
#        data_2 = json.loads(response_2.read().decode('utf-8'))
#        print(data_2)
#    except json.JSONDecodeError as e:
#        print(f"Error decoding JSON for {result_url}: {e}")
#    except Exception as e:
#        print(f"Error fetching data from {result_url}: {e}")
