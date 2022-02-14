from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.station import MonitoringStation


stations = build_station_list()

update_water_levels(stations)

tol = 0.0

#over_threshold = stations_level_over_threshold(stations, tol)

#print (over_threshold)

for station in stations: 
    fraction = station.relative_water_level()
    tuple = (station.name, station.latest_level, station.typical_range, fraction)
    print (tuple)