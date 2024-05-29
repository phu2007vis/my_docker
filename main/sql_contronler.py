import os
import mysql.connector
import pandas as pd
import atexit

# Fetch environment variables
sql_endpoint = os.getenv('SQL_ENDPOINT')
sql_user = os.getenv('SQL_USER', 'admin')
sql_password = os.getenv('SQL_PASSWORD', 'phuocvip1')
database = os.getenv('SQL_DATABASE', 'phuoc')

connection = None
cursor = None

def connect_to_database():
    global connection, cursor
    try:
        connection = mysql.connector.connect(
            host=sql_endpoint,
            sql_user=sql_user,
            sql_password=sql_password,
            database=database
        )
        cursor = connection.cursor()
        print("SQL connected successfully")
    except mysql.connector.Error as e:
        print("Error connecting to MySQL", e)

def close_database_connection():
    global connection
    if connection:
        connection.close()
        print("SQL connection closed")

def create_person_table():
    try:
        command = """
        CREATE TABLE IF NOT EXISTS person (
            tk VARCHAR(255) NOT NULL,
            mk VARCHAR(255) NOT NULL,
            PRIMARY KEY (tk, mk)
        );
        """
        cursor.execute(command)
        connection.commit()
        print("Table 'person' is ready")
    except mysql.connector.Error as e:
        print("Error while creating table", e)


def insert_new_person(tk: str, mk: str):
    try:
        command = "INSERT INTO person (tk, mk) VALUES (%s, %s);"
        cursor.execute(command, (tk, mk))
        connection.commit()
        return [None]
    except mysql.connector.Error as e:
        print("Error while inserting into MySQL", e)
        return [e]

def check_login(tk: str, mk: str):
    try:
        command = "SELECT * FROM person WHERE tk = %s AND mk = %s;"
        cursor.execute(command, (tk, mk))
        results = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(results, columns=column_names)
        return [df, None]
    except mysql.connector.Error as e:
        print("Error while querying MySQL", e)
        return [None, e]

atexit.register(close_database_connection)
connect_to_database()
create_person_table()

if __name__ == "__main__":
    pass
