"""Unit tests for functions in the flood module"""
from test_station import test_create_monitoring_station
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.flood import stations_highest_rel_level
from floodsystem.station import MonitoringStation


def test_stations_highest_rel_level():

    test_station = test_create_monitoring_station() #create test monitoring station
    test_station.latest_level = 1.0 #give test station a latest level value
    test_station_list = [] #create a list to pass to the function so data is in correct form
    test_station_list.append(test_station) 

    top_N1 = stations_highest_rel_level(test_station_list, 1) #call function to check if over threshold
    top_N0 = stations_highest_rel_level(test_station_list, 0) #call function to check if over threshold

    assert top_N1 != []
    assert top_N0 == []

test_stations_highest_rel_level()