
from urllib.request import urlopen
import json
import psycopg2
import api


# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="postgres",
    user="",
    password="",
    host="localhost",
    port="5432"
)

# Create a cursor object
cur = conn.cursor()

# Create table for session data
create_table_session = """
CREATE TABLE IF NOT EXISTS sessions (
    id SERIAL PRIMARY KEY,
    circuit_key int,
    circuit_name varchar(100),
    country VARCHAR(100),
    country_code varchar(100),
    session_type VARCHAR(100),
    session_key int
)
"""


# Create table for drivers data
create_table_drivers = """
CREATE TABLE IF NOT EXISTS drivers (
    id SERIAL PRIMARY KEY,
    driver_number int,
    session_key int,
    broadcast_name varchar(100),
    name_acronym varchar(100),
    first_name varchar(100),
    last_name varchar(100),
    team_name varchar(100)
)
"""

# Create table for positions data
create_table_positions = """
CREATE TABLE IF NOT EXISTS positions (
    id SERIAL PRIMARY KEY,
    driver_number int,
    session_key int,
    position int,
    date timestamp
)
"""

#execute create sessions table
cur.execute(create_table_session)
conn.commit()

#execute create drivers table
cur.execute(create_table_drivers)
conn.commit()

#execture create postitions table
cur.execute(create_table_positions)
conn.commit()

#using the openf1 API's call data re ressions
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

session_url = base + methods[0] + variables[0] + year + "&session_key=9222"
response = urlopen(session_url)
session_data = json.loads(response.read().decode('utf-8'))
session_key = [item["session_key"] for item in session_data]
country_code = [item["country_code"] for item in session_data]
session_type = [item["session_type"] for item in session_data]
circuit_name = [item["circuit_short_name"] for item in session_data]
circuit_key = [item["circuit_key"] for item in session_data]
combined_data_session = list(zip(session_key, country_code,session_type,circuit_name,circuit_key))

print(combined_data_session)

# Process each session
for key in session_key:
    driver_url = base + methods[2] + variables[2] + str(key)
    response = urlopen(driver_url)
    driver_data = json.loads(response.read().decode('utf-8'))
    broadcast_name = [item["broadcast_name"] for item in driver_data]
    driver_number = [item["driver_number"] for item in driver_data]
    session_key_driver = key
    team_name = [item["team_name"] for item in driver_data]
    first_name = [item["first_name"] for item in driver_data]
    last_name = [item["last_name"] for item in driver_data]
    name_acronym = [item["name_acronym"] for item in driver_data]
    combined_data_driver = list(zip(broadcast_name, driver_number, str(session_key_driver), team_name,first_name,last_name,name_acronym))
    print(combined_data_driver)

    # Fetch position data for each session

    position_url = base + methods[8] + variables[2] + str(key)
    response = urlopen(position_url)
    position_data = json.loads(response.read().decode('utf-8'))
    driver_number_position = [item["driver_number"] for item in position_data]
    session_key_position = key
    position = [item["position"] for item in position_data]
    date = [item["date"] for item in position_data]

    combined_data_position = list(zip(driver_number_position, str(session_key_position), position, date))
    print(combined_data_position)

#insert data into sessions table
insert_query = """
INSERT INTO sessions (session_key,country_code,session_type,circuit_name,circuit_key) VALUES (%s, %s, %s, %s, %s)
"""

cur.executemany(insert_query,combined_data_session)
conn.commit()


# Insert data into drivers table
insert_query = """
INSERT INTO drivers (broadcast_name,driver_number,session_key,team_name,first_name,last_name,name_acronym) VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

cur.executemany(insert_query,combined_data_driver)
conn.commit()

# Insert data into positions table
insert_query = """
INSERT INTO positions (driver_number,session_key,position,date) VALUES (%s, %s, %s, %s)
"""

cur.executemany(insert_query,combined_data_position)
conn.commit()

# Close the cursor and connection
cur.close()