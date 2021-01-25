import sys
import os

import sqlite3
from sqlite3 import Error
import configparser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists

from SatelliteLocator.Database.createDatabase import createDatabase
from SatelliteLocator.Database import base
from SatelliteLocator.Entities.SAT import SAT
from SatelliteLocator.Entities.LOC import LOC

class SATRepository:
    def __init__(self):
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
        
        if not os.path.exists(db_file) or os.stat(db_file).st_size == 0:
            createDatabase()

        engine = create_engine("sqlite:///" + db_file, echo=True)
        base.Base.metadata.create_all(engine, checkfirst=True)
        Session = sessionmaker(bind=engine)
        self.session = Session()
    
    def get_sat_by_id(self, catalog_number):
        return self.session.query(SAT.catalog_number).filter(SAT.catalog_number == catalog_number).first()

    def get_loc_by_date(self, sat_id, date):
        return self.session.query(LOC.sat_id).filter(LOC.sat_id == sat_id and LOC.date == date).first()

    def create_sat(self, entity):
        self.session.add(entity)
        self.session.commit()

    def create_loc(self, entity):
        self.session.add(entity)
        self.session.commit()