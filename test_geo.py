"""Unit tests for functions in the geo module"""

from sqlalchemy import true
from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation 
from floodsystem.geo import stations_within_radius
from test_station import test_create_monitoring_station
from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number

stations = build_station_list()

def test_stations_by_distance():
    """This function tests that the stations_by_distance function correctly
    calculates the distance between a station and given point."""

    """s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    test_station = MonitoringStation(s_id, m_id, label, coord, trange, river, town)"""
    
    #Create a test station
    test_station = test_create_monitoring_station()
    test_station_list = [] #create a list to pass to the function so data is in correct form
    test_station_list.append(test_station)
    p = (52.2053,0.1218)

    stations_distance = stations_by_distance(test_station_list, p) #call function

    distance = abs(stations_distance[0][2] - 6038.3717730613525) #calculate difference between calculated distance value and correct value

    assert distance <= 0.00001 

def test_stations_within_radius():
    """This function tests whether the function excludes a station
     from the list if it is out of radius."""
     
    test_station = test_create_monitoring_station()
    test_station_list = [] #create a list to pass to the function so data is in correct form
    test_station_list.append(test_station)
    centre = (52.2053,0.1218) #distance to measure from 
    radius = 6038

    stations_within = stations_within_radius(test_station_list, centre, radius)

    assert stations_within == []

def test_rivers_with_station():
    "This function tests that the function can be called successfully"
    x = rivers_with_station(stations)
    assert type(x) == set



def test_stations_by_river():
    "This function tests that the function maps a river to its monitoring station"
    test_station = test_create_monitoring_station()
    test_station_list = []
    test_station_list.append(test_station)
    y = stations_by_river(test_station_list)

    assert y == {'River X': ['some station']}


def test_rivers_by_station_number():
    "This function tests that the function returns a list of tuples"
    z = rivers_by_station_number(stations, N = 1)
    assert all(isinstance(item, tuple) for item in z)

