import os
import mysql.connector
import pandas as pd
import atexit

# Fetch environment variables
sql_endpoint = os.getenv('SQL_ENDPOINT',"database-1.cxlucbxeycgv.us-east-1.rds.amazonaws.com")
sql_user = os.getenv('SQL_USER', 'admin')
sql_password = os.getenv('SQL_PASSWORD', 'phuocvip1')
database = os.getenv('SQL_DATABASE', 'phuoc')
print(sql_endpoint)
print(sql_user)
print(sql_password)
connection = None
cursor = None

def connect_to_database():
    global connection, cursor
    try:
        connection = mysql.connector.connect(
             host=sql_endpoint,
                user=sql_user,
                password=sql_password,
                # database=database
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
       # Create the database if it does not exist
        command = 'CREATE DATABASE IF NOT EXISTS phuoc'
        cursor.execute(command)
        connection.commit()

        # Use the newly created database
        command = 'USE phuoc'
        cursor.execute(command)

        # Create the table if it does not exist
        command = """
        CREATE TABLE IF NOT EXISTS person (
            tk VARCHAR(255) NOT NULL,
            mk VARCHAR(255) NOT NULL,
            PRIMARY KEY (tk)
        );
        """
        cursor.execute(command)
        connection.commit()
        if not check_login_sql('admin','1'):
            insert_new_person('admin','1')
            
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

def check_login_sql(tk: str, mk: str):
    try:
            command = "SELECT * FROM person WHERE tk = %s AND mk = %s;"
            cursor.execute(command, (tk, mk))
            results = cursor.fetchall()
            return len(results) > 0
    except mysql.connector.Error as e:
        print("Error while querying MySQL", e)
        return False

atexit.register(close_database_connection)
connect_to_database()
create_person_table()

if __name__ == "__main__":
    pass
