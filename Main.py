
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
    session_key int,
    country VARCHAR(100),
    session_type VARCHAR(100)
)
"""

# Create table for drivers data
create_table_drivers = """
CREATE TABLE IF NOT EXISTS drivers (
    id SERIAL PRIMARY KEY,
    broadcast_name varchar(100),
    driver_number int,
    session_key int,
    team_name varchar(100)
)
"""

# Create table for positions data
create_table_positions = """
CREATE TABLE IF NOT EXISTS postitions (
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

# Fetching session data
session_url = base + methods[0] + variables[0] + year
response = urlopen(session_url)
session_data = json.loads(response.read().decode('utf-8'))
session_keys = [item["session_key"] for item in session_data]
country_code = [item["country_code"] for item in session_data]
session_type = [item["session_type"] for item in session_data]

combined_data_session = list(zip(session_keys, country_code,session_type))

# Insert data
insert_query = """
INSERT INTO sessions (session_key,country,session_type) VALUES (%s, %s, %s)
"""

#insert data into sessions table
cur.executemany(insert_query,combined_data_session)
conn.commit()

# Close the cursor and connection
cur.close()