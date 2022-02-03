from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import inconsistent_typical_range_stations

stations = build_station_list() #builds list of stations

inconsistent_stations =  inconsistent_typical_range_stations(stations) 

print (inconsistent_stations)