from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.station import MonitoringStation


stations = build_station_list()
update_water_levels(stations)
tol = 0.8

over_level = stations_level_over_threshold(stations, tol)


for station in over_level: 
    print (str(station[0]) + " " + str(station[1]))

