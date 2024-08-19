import psycopg2

# This file takes an empty database and will run a SQL file to create all needed tables and the references between tables

# Open the schema file
with open('./data/schema.sql', 'r') as file:
    sql_script = file.read()

# Connect to local DB

    conn = psycopg2.connect(
        dbname="f1",
        user="",
        password="",
        host="localhost",
        port="5432"
    )

    # Create a cursor to execute the SQL script
    cursor = conn.cursor()

    # Run .sql file to create database schema
    create_commands = sql_script.split(';')
    for create in create_commands:
        try:
            cursor.execute(create)
            print("Database bootstrapped successfully.")
        except Exception as e:
            print(f"Database bootstrapped NOT successfully because {e}")

    # Commit the transaction to DB
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()