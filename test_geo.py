"""Unit test for sort_by_distance function in the geo module"""

from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation 
#from floodsystem.stationdata import build_station_list

def test_stations_by_distance():

# Create a test station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    test_station = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    test_station_list = []

    test_station_list.append(test_station)

    p = (52.2053,0.1218)

    stations_distance = stations_by_distance(test_station_list, p)

    x = abs(stations_distance[0][2] - 6038.3717730613525)

    assert x <= 0.00001





#test haversine 

#test sort order 

#test sort order is high to low 


