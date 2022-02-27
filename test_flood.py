"""Unit tests for functions in the flood module"""
from test_station import test_create_monitoring_station
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.station import MonitoringStation


def test_stations_level_over_threshold():
    """This function tests the stations_level_over_threshold 
    function in the flood module."""

    test_station = test_create_monitoring_station() #create test monitoring station
    test_station.latest_level = 1.0 #give test station a latest level value
    test_station_list = [] #create a list to pass to the function so data is in correct form
    test_station_list.append(test_station) 
    tol = 0.5 #tolerence that is just below the relative level of test station 

    test_over_level = stations_level_over_threshold(test_station_list, tol) #call function to check if over threshold

    """print (test_station)
    print (test_station_list)
    print (test_over_level)"""

    assert test_over_level != [] #assert to check a list item is returned

def test_stations_highest_rel_level():
    """This function tests the stations_highest_rel_level 
    function in the flood module."""

    test_station = test_create_monitoring_station() #create test monitoring station
    test_station.latest_level = 1.0 #give test station a latest level value
    test_station_list = [] #create a list to pass to the function so data is in correct form
    test_station_list.append(test_station) 

    top_N1 = stations_highest_rel_level(test_station_list, 1) #call function to check if over threshold
    top_N0 = stations_highest_rel_level(test_station_list, 0) #call function to check if over threshold

    assert top_N1 != []
    assert top_N0 == []
 


