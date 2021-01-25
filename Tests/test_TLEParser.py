import pytest

from SatelliteLocator.TLEParser import TLEParser

class TestTLEParser:

    def test_tle_string(self, mocker):
        entity = "1 25544U 98067A   21025.26149851  .00001023  00000-0  26803-4 0  9995\n\n2 25544  51.6462 329.6445 0002275 288.5035 166.1954 15.48884405266447"

        mocker.patch(
            "SatelliteLocator.TLEParser.retrieveTleString",
            return_value = entity
        )

        test_sat, test_loc = TLEParser()

        assert test_sat.catalog_number == 25544
        assert test_loc.sat_id == 25544

    def test_parser_math(self, mocker):
        entity = "1 25544U 98067A   21025.26149851  .00001023  00000-0  26803-4 0  9995\n\n2 25544  51.6462 329.6445 0002275 288.5035 166.1954 15.48884405266447"

        mocker.patch(
            "SatelliteLocator.TLEParser.retrieveTleString",
            return_value = entity
        )

        test_sat, test_loc = TLEParser()

        assert test_sat.launch_year == 1998
        assert test_loc.first_deriv_mean == 1.023e-05
        assert test_loc.second_deriv_mean == 0.0
        assert test_loc.mean_motion == 15.48884405
        assert test_loc.rev_number_at_epoch == 26644