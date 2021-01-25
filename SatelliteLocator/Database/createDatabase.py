import sqlite3
from sqlite3 import Error
import configparser

def createDbConnection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def createDatabase():

    # ACTION REQUIRED FOR YOU:
    #=========================
    # Provide a config file in the same directory as this file, called DB.ini, with this format (without the # signs)
    # [database_configuration]
    # db_file = XXX
    # sql_file = YYY
    #
    # ... where XXX is the path to your database file
    # ... and YYY is the path to your sql file 

    # Use configparser package to pull in the ini file
    config = configparser.ConfigParser()
    config.read("SatelliteLocator/Database/DB.ini")
    db_file = config.get("database_configuration","db_file")
    sql_file = config.get("database_configuration","sql_file")

    conn = createDbConnection(db_file)

    if conn is not None:
        c = conn.cursor()

        sqlFile = open(sql_file)
        sql_as_string = sqlFile.read()
        c.executescript(sql_as_string)
    else:
        print("Error! Cannot create the database connection.\nFormat of input: \"Path/to/database.db\"")

if __name__ == '__main__':
    createDatabase()