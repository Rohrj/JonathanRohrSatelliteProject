import sqlite3
from sqlite3 import Error

def createDbConnection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

if __name__ == '__main__':
    createDbConnection(r"Database/SatelliteInfo.db")