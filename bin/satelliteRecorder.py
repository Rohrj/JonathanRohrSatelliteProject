import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from SatelliteLocator.satelliteService import satelliteService
from SatelliteLocator.TLEParser import TLEParser
from SatelliteLocator.Database import base
from SatelliteLocator.Entities.SAT import SAT
from SatelliteLocator.Entities.LOC import LOC
from SatelliteLocator.Entities import databaseRepository

def main(argv):
    if len(argv) == 0:
        print("Usage: main.py <NORAD ID 1> <NORAD ID 2> ...")
        sys.exit(2)
    elif argv[0] == None or argv[0] == "-h" or argv[0] == "-help" or argv[0] == "h" or argv[0] == "help":
        print("Usage: main.py <NORAD ID 1> <NORAD ID 2> ...")
        sys.exit(2)
    else:
        sat_repo = databaseRepository.SATRepository()
        for x in argv:
            satelliteService(x)

            SatInst, LocInst = TLEParser()

            if sat_repo.get_sat_by_id(SatInst.catalog_number) is None:
                sat_repo.create_sat(SatInst)
            elif sat_repo.get_loc_by_date(LocInst.sat_id, LocInst.date) is None:
                sat_repo.create_loc(LocInst)
            else:
                print(f"\nThe satellite with the id: {x} already has entries in both tables for that date and time.\n")
                pass

if __name__ == '__main__':
    main(sys.argv[1:])