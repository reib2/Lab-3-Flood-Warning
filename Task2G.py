from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.flood import flood_warning

#build list and splice
stations = build_station_list() 
update_water_levels(stations)
#stations_list = stations[:50]

N = 40
top_N = stations_highest_rel_level(stations, N)
station_list = []
for station in top_N: 
    station_list.append(station[0])


flood_warning(station_list)