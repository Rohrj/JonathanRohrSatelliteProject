import sys
import math

import skyfield.api
import skyfield.elementslib
import configparser

from SatelliteLocator.Entities.SAT import SAT
from SatelliteLocator.Entities.LOC import LOC

def retrieveTleString():
    config = configparser.ConfigParser()
    config.read("SatelliteLocator/SLTrack.ini")
    configOut = config.get("configuration","output")

    with open(configOut, "r") as file:
        tle_string = file.read()
    return tle_string

def retrieveSatellite():
    tle_string = retrieveTleString()
    tle_lines = tle_string.strip().splitlines()

    try:
        tle_lines = tle_string.strip().splitlines()
        if(len(tle_lines) > 3):
            satellite = skyfield.api.EarthSatellite(tle_lines[2], tle_lines[4], tle_lines[0])
        elif(len(tle_lines) == 3):
            satellite = skyfield.api.EarthSatellite(tle_lines[0], tle_lines[2], "UNKNOWN")
        else:
            raise Exception("TLE data needs at least two lines.")
    except Exception as e:
        print("Unable to decode TLE data. Make the sure TLE data is formatted correctly." + e)
        exit(1)
    
    return satellite

def TLEParser():
    satellite = retrieveSatellite()

    if int(satellite.model.intldesg[0:2]) >= 57:
        launch_year = int("19" + satellite.model.intldesg[0:2])
    else:
        launch_year = int("20" + satellite.model.intldesg[0:2])
    
    xpdotp = 1440.0 / (2.0 * math.pi)
    
    SatInst = SAT(catalogNumber = satellite.model.satnum, 
                    classification = satellite.model.classification, 
                    launchYear = launch_year, 
                    launchNumAndDesignator = satellite.model.intldesg[2:])
    
    LocInst = LOC(catalogNumber = satellite.model.satnum, 
                    date = satellite.epoch.utc_iso(), 
                    firstDerivMean = satellite.model.ndot * xpdotp * 1440.0, 
                    secondDerivMean = satellite.model.nddot * xpdotp * 1440.0 * 1440.0, 
                    dragTerm = satellite.model.bstar, 
                    elemSetNumber = satellite.model.elnum, 
                    inclination = math.degrees(satellite.model.inclo), 
                    rightAsc = math.degrees(satellite.model.nodeo), 
                    eccentricity = satellite.model.ecco, 
                    argPerigree = math.degrees(satellite.model.argpo), 
                    meanAnomaly = math.degrees(satellite.model.mo), 
                    meanMotion = (satellite.model.no_kozai * 60 * 24) / (2 * math.pi), 
                    revNumberAtEpoch = satellite.model.revnum)

    return SatInst, LocInst