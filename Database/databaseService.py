import sys
import os

import sqlite3
from sqlite3 import Error
import configparser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists

from Database.createDatabase import createDatabase
from Database import base
from Data.SAT import SAT
from Data.LOC import LOC

def databaseService(SatInst, LocInst):
    
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
    config.read("Database/DB.ini")
    db_file = config.get("database_configuration","db_file")
    
    if not os.path.exists(db_file) or os.stat(db_file).st_size == 0:
        createDatabase()

    engine = create_engine("sqlite:///" + db_file, echo=True)
    base.Base.metadata.create_all(engine, checkfirst=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    exists = session.query(SAT.catalog_number).filter(SAT.catalog_number == SatInst.catalog_number).first()
    if exists is None:
        session.add(SatInst)

    session.add(LocInst)
    session.commit()

if __name__ == '__main__':
    databaseService(sys.argv[0], sys.argv[1])