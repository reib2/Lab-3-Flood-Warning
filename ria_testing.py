#testing for 1F

from floodsystem import datafetcher
from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list


stations = build_station_list() #builds list of stations 

single_station = stations[0]

inconsistent_stations =  single_station.typical_range_consistent()

print (inconsistent_stations)





"""Unit test for sort_by_distance function in the geo module"""
""""
import floodsystem.geo 
from floodsystem.stationdata import build_station_list
from haversine import haversine, Unit #import haversine function from library



def test_stations_by_distance():
    stations = build_station_list()

""""


#test haversine 

#test sort order 

#test sort order is high to low 


