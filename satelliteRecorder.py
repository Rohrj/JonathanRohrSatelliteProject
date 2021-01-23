import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Service.satelliteService import satelliteService
from Parser.TLEParser import TLEParser
from Database import databaseService
from Database import base
from Data.SAT import SAT
from Data.LOC import LOC

def main(argv):
    if len(argv) == 0:
        print("Usage: main.py <NORAD ID 1> <NORAD ID 2> ...")
        sys.exit(2)
    elif argv[0] == None or argv[0] == "-h" or argv[0] == "-help" or argv[0] == "h" or argv[0] == "help":
        print("Usage: main.py <NORAD ID 1> <NORAD ID 2> ...")
        sys.exit(2)
    else:
        sat_repo = databaseService.SATRepository()
        for x in argv:
            satelliteService(x)

            SatInst, LocInst = TLEParser()

            if sat_repo.get_by_id(SatInst.catalog_number) is None:
                sat_repo.create_sat(SatInst)
            sat_repo.create_loc(LocInst)

if __name__ == '__main__':
    main(sys.argv[1:])