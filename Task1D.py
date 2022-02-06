from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station

stations = build_station_list()
rivers = rivers_with_station(stations)
number = len(rivers)
first = list(sorted(rivers))[:10]


print(number, 'stations. First 10 -', first)
