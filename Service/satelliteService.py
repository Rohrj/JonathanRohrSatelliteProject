import sys

import requests
import configparser

from Service import errorHandling

def satelliteService(input):

    # See https://www.space-track.org/documentation for details on REST queries
    # The "Find Starlinks" query searches for satellite with NORAD_CAT_ID = specified Id (from input)
    # Example URL: https://www.space-track.org/basicspacedata/query/class/tle_latest/NORAD_CAT_ID/25544/ORDINAL/1/format/tle

    uriBase = "https://www.space-track.org"
    requestLogin = "/ajaxauth/login"
    requestCmdAction = "/basicspacedata/query"
    requestFindStarlinks1 = "/class/tle_latest/NORAD_CAT_ID/"
    noradCatId = input
    requestFindStarlinks2 = "/ORDINAL/1/format/tle"

    # ACTION REQUIRED FOR YOU:
    #=========================
    # Provide a config file in the same directory as this file, called SLTrack.ini, with this format (without the # signs)
    # [configuration]
    # username = XXX
    # password = YYY
    # output = ZZZ
    #
    # ... where XXX and YYY are your www.space-track.org credentials (https://www.space-track.org/auth/createAccount for free account)
    # ... and ZZZ is your TLE Output file - e.g. starlink-track.tle

    # Use configparser package to pull in the ini file
    config = configparser.ConfigParser()
    config.read("Service/SLTrack.ini")
    configUsr = config.get("configuration","username")
    configPwd = config.get("configuration","password")
    configOut = config.get("configuration","output")
    siteCred = {'identity': configUsr, 'password': configPwd}

    # use requests package to drive the RESTful session with space-track.org
    with requests.Session() as session:
        # run the session in a with block to force session to close if we exit

        # need to log in first. note that we get a 200 to say the web site got the data, not that we are logged in
        resp = session.post(uriBase + requestLogin, data = siteCred)
        if resp.status_code != 200:
            raise errorHandling.Error(resp, "POST fail on login")

        # this query picks up all Starlink satellites from the catalog. Note - a 401 failure shows you have bad credentials 
        resp = session.get(uriBase + requestCmdAction + requestFindStarlinks1 + noradCatId + requestFindStarlinks2)
        if resp.status_code != 200:
            print(resp)
            raise errorHandling.Error(resp, "GET fail on request for Starlink satellites")

        # open the starlink-track.tle file to store the response from the api call
        with open(configOut, "w") as f:
            f.write(resp.text)

        session.close()
    #print("Completed session")