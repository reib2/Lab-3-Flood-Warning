#testing for 1F

from floodsystem import datafetcher
from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list


stations = build_station_list() #builds list of stations 

single_station = stations[0]

inconsistent_stations =  single_station.typical_range_consistent()

print (inconsistent_stations)



