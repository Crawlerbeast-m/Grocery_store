import mysql.connector
import datetime

__cnx = None

def get_sql_connection():
    print("Connecting to the database...")
    global __cnx
    if __cnx is None:
        try:
            __cnx = mysql.connector.connect(user='root',
                                            host='localhost',
                                            password='',
                                            port=3306,
                                            database='grocery_store')
            print("Connected to the database...")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            __cnx = None
        except Exception as e:
            print(f"Unexpected error: {e}")
            __cnx = None
    return __cnx