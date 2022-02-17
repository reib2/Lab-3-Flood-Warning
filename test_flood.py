"""Unit tests for functions in the flood module"""
from test_station import test_create_monitoring_station

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.station import MonitoringStation


def test_stations_level_over_threshold():
    """This function tests the stations_level_over_threshold 
    function in the flood module."""

    test_station = test_create_monitoring_station()
    test_station_list = [] #create a list to pass to the function so data is in correct form
    test_station_list.append(test_station)

    tol = 0.0

    #test_over_level = stations_level_over_threshold(test_station_list, tol)

    #assert test_over_level[0] != None



