import skyfield.api
import skyfield.elementslib
import sys
import math

from Data.SAT import SAT
from Data.LOC import LOC

def retrieveTleString():
    with open("Service/starlink-track.txt", "r") as file:
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

    catalog_num = satellite.model.satnum

    classification = satellite.model.classification

    if int(satellite.model.intldesg[0:2]) >= 57:
        launch_year = int("19" + satellite.model.intldesg[0:2])
    else:
        launch_year = int("20" + satellite.model.intldesg[0:2])

    launch_num_and_des = satellite.model.intldesg[2:]

    date = satellite.epoch.utc_iso()

    xpdotp = 1440.0 / (2.0 * math.pi)
    first_deriv_mean = satellite.model.ndot * xpdotp * 1440.0
    second_deriv_mean = satellite.model.nddot * xpdotp * 1440.0 * 1440.0

    drag = satellite.model.bstar

    elem_set_num = satellite.model.elnum

    inclination = math.degrees(satellite.model.inclo)

    right_asc = math.degrees(satellite.model.nodeo)

    eccentricity = satellite.model.ecco

    arg_perigree = math.degrees(satellite.model.argpo)

    mean_anomaly = math.degrees(satellite.model.mo)

    mean_motion = (satellite.model.no_kozai * 60 * 24) / (2 * math.pi)

    rev_num_at_epoch = satellite.model.revnum
    
    SatInst = SAT(catalog_num, classification, launch_year, launch_num_and_des)
    
    LocInst = LOC(catalog_num, date, first_deriv_mean, second_deriv_mean, drag, elem_set_num, inclination, right_asc, 
                eccentricity, arg_perigree, mean_anomaly, mean_motion, rev_num_at_epoch)

    return SatInst, LocInst