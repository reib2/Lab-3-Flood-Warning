from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

#builds list of stations
stations = build_station_list()

#distance to measure from 
p = (52.2053,0.1218)

#returns list of stations sorted by distance 
stations_by_distance(stations, p)