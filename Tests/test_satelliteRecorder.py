import pytest

from bin import satelliteRecorder

class TestSatelliteRecorder:
    
    def test_program_works(self):
        
        print("Adding entries in table for NORAD IDs: 25544, 47344, 47303")
        satelliteRecorder.main(["25544", "47344", "47303"])

    def test_program_bad_input(self):

        print("Testing error handling by passing in bad input")
        satelliteRecorder.main(["3499382939"])

    def test_program_no_input(self):

        print("Testing error handling by passing in no input")
        satelliteRecorder.main([None])