#testing for 1F
"""
from floodsystem import datafetcher
from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list


stations = build_station_list() #builds list of stations 

single_station = stations[0]

inconsistent_stations =  single_station.typical_range_consistent()

print (inconsistent_stations)

"""

from haversine import haversine, Unit #import haversine function from library
x = haversine((-2.0, 4.0), (52.2053,0.1218) )
print (x)

from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation 
from floodsystem.geo import stations_within_radius
from test_station import test_create_monitoring_station

def test_stations_within_radius():

    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    test_station = MonitoringStation(s_id, m_id, label, coord, trange, river, town)    

    test_station_list = [] #create a list to pass to the function so data is in correct form
    test_station_list.append(test_station)
    centre = (52.2053,0.1218) #distance to measure from 
    radius = 6038

    stations_within = stations_within_radius(test_station_list, centre, radius)
    
    assert stations_within == []

test_stations_within_radius()