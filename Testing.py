
from urllib.request import urlopen
import json
import pandas as pd
import psycopg2


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

# Create table if it doesn't exist
create_table_query_session = """
CREATE TABLE IF NOT EXISTS sessions (
    id SERIAL PRIMARY KEY,
    session_key VARCHAR(100),
    country VARCHAR(100),
    session_type VARCHAR(100)
)
"""
create_table_query_drivers = """
CREATE TABLE IF NOT EXISTS drivers (
    id SERIAL PRIMARY KEY,

)
"""
create_table_positions = """
CREATE TABLE IF NOT EXISTS postitions (
    id SERIAL PRIMARY KEY,
    driver_number int,
    position int,
    session_key int
)
"""
cur.execute(create_table_query)
conn.commit()

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
country_code = [item["country_code"] for item in data]
session_type = [item["session_type"] for item in data]

combined_data = list(zip(session_keys, country_code,session_type))

# Insert data
insert_query = """
INSERT INTO sessions (session_key,country,session_type) VALUES (%s, %s, %s)
"""
cur.executemany(insert_query,combined_data)
conn.commit()

# Close the cursor and connection
cur.close()