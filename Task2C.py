from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.station import MonitoringStation


stations = build_station_list()
update_water_levels(stations)
N = 10 

top_ten = stations_highest_rel_level(stations, N)


for station in top_ten: 
    print (str(station[0]) + " " + str(station[1]))



"""
list = [1,2,3,4]
print (list[:2])"""

