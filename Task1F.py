
from floodsystem import datafetcher
from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

stations = build_station_list() #builds list of stations

inconsistent_stations =  inconsistent_typical_range_stations(stations) 

print (inconsistent_stations)



