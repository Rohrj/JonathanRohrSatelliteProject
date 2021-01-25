# Satellite Locator

Jonathan Rohr


Important packages to install (if not installed already):
- pip install sqlite3
- pip install sqlalchemy
- pip install requests
- pip install skyfield
- pip install pytest


Instructions to run program:
- Clone or download from github
- Open a terminal and navigate to /JonathanRohrSatelliteProject
- Install above packages
- Open the config file /SatelliteLocator/SLTrack.ini
- In SLTrack.ini, replace the username and password values with your username and password for https://www.space-track.org/ (make a free account if you don't have login credentials)
- The output file can be left alone unless you would like to change the name
- Then run `python -m bin.satelliteRecorder [NORAD ID 1] [NORAD ID 2] ...`
- https://www.n2yo.com/ is a good source of NORAD IDs although not all of them are present in space-track's database
- If no errors are raised, the results should appear in the database in their respective tables (SAT and LOC)


Program description:

This program accepts the NORAD ID(s) of one or more satellites as input. If the id is not present in the space-track database or a bad input is given, an error will be raised and no data will be stored in the database. If the id is present, space-track's RESTful API will return the TLE data for the ID and store it in a seperate file named startrack-tle.txt. The TLEParser module will then read that file and parse through the TLE data using an open source library called Skyfield. The parsed data is then stored in SAT and LOC classes that are connected to the sqlite database using Sqlalchemy so they can be easily inserted into the local database.

A pair of functions check the SAT and LOC tables for two specific conditions before proceeding with the data insertions. The first makes sure that the SAT table does not contain an entry with the same catalog_number (NORAD ID). If it does, then no entry is inserted. The second function checks the LOC table for an entry with the same sat_id (NORAD ID) AND the same date and time. This is to prevent duplicate entries in the LOC table while also allowing new data (same id, but different date and time) to be inserted. If both tables already contain the data, a message will be printed and the program will move on to the next NORAD ID.

The provided EmptyDatabase.sql contains the schema for a brand new database with the appropriate data. That file can be switched out for an existing table (with the same structure) in the /SatelliteLocator/Database/DB.ini file.

Each time the program is run, it checks first to see if there is a database already in existance. It will create a database and create the tables using the sql schema if no database exists. This is why there is no need to create a database first before running the program on a new system.

I have created a few unit and integration tests in the Tests folder. The unit tests make sure that the TLE data is in the proper format and is parsed correctly by the Skyfield api. They also check the minor math calculations that are performed on some of data to convert them to the proper units. The integration tests test the program itself to ensure that it can take in multiple inputs and store them all in the database. They also test if the inputs are bad or if there is no inputs.