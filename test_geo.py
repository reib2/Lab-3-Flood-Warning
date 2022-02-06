"""Unit test for functions in the geo module"""

from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation 
from floodsystem.geo import stations_within_radius
from test_station import test_create_monitoring_station

#from floodsystem.stationdata import build_station_list


def test_stations_by_distance():
    """This function tests that the stations_by_distance function correctly
    calculates the distance between a station and given point."""

# Create a test station
    """s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    test_station = MonitoringStation(s_id, m_id, label, coord, trange, river, town)"""

    test_station = test_create_monitoring_station()

    test_station_list = [] #create a list to pass to the function so data is in correct form
    test_station_list.append(test_station)
    p = (52.2053,0.1218)

    stations_distance = stations_by_distance(test_station_list, p) #call function

    distance = abs(stations_distance[0][2] - 6038.3717730613525) #calculate difference between calculated distance value and correct value

    assert distance <= 0.00001 

def test_stations_within_radius():
