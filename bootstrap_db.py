import psycopg2

# This file takes an empty database and will run a SQL file to create all needed tables and the references between tables

# Open the schema file
with open('./data/schema.sql', 'r') as file:
    sql_script = file.read()

# Connect to local DB
conn=psycopg2.connect(
    dbname="postgres",
    user="",
    password="",
    host="localhost",
    port="5432"
    )


# Create a cursor to execute the SQL script
cursor = conn.cursor()

# Run .sql file to create database schema
cursor.execute(sql_script)
conn.commit()
print("SQL script executed successfully.")

# Close the cursor and connection
cursor.close()
conn.close()

##LINE 11: CREATE TABLE "driver_metadata" ERROR