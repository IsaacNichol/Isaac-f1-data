# main.py
from api_calls import API
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

# Execute create sessions table
cur.execute(create_table_session)
conn.commit()

# Execute create drivers table
cur.execute(create_table_drivers)
conn.commit()

# Execute create positions table
cur.execute(create_table_positions)
conn.commit()

# Using the OpenF1API class
base_url = 'https://api.openf1.org/v1/'
api = API(base_url)

year = '2023'
session_data = api.get_sessions(year)
combined_data_session = api.process_session_data(session_data)

print(combined_data_session)

# Initialize lists to collect all driver and position data
all_combined_data_driver = []
all_combined_data_position = []

# Process each session
for session in session_data:
    session_key = session["session_key"]

    driver_data = api.get_drivers(session_key)
    combined_data_driver = api.process_driver_data(driver_data, session_key)
    all_combined_data_driver.extend(combined_data_driver)
    print(combined_data_driver)

    position_data = api.get_positions(session_key)
    combined_data_position = api.process_position_data(position_data, session_key)
    all_combined_data_position.extend(combined_data_position)
    print(combined_data_position)

# Insert data into sessions table
insert_query = """
INSERT INTO sessions (session_key, country_code, session_type, circuit_name, circuit_key) VALUES (%s, %s, %s, %s, %s)
"""
cur.executemany(insert_query, combined_data_session)
conn.commit()

# Insert data into drivers table
insert_query = """
INSERT INTO drivers (broadcast_name, driver_number, session_key, team_name, first_name, last_name, name_acronym) VALUES (%s, %s, %s, %s, %s, %s, %s)
"""
cur.executemany(insert_query, all_combined_data_driver)
conn.commit()

# Insert data into positions table
insert_query = """
INSERT INTO positions (driver_number, session_key, position, date) VALUES (%s, %s, %s, %s)
"""
cur.executemany(insert_query, all_combined_data_position)
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
