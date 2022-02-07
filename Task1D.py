from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

stations = build_station_list()
rivers = rivers_with_station(stations)
number = len(rivers)
first = list(sorted(rivers))[:10]


print(number, 'stations. First 10 -', first)

river_stations = stations_by_river(stations)

river_names = ['River Aire', 'River Cam', 'River Thames']
sorted_stations = []

for i in river_names:
    river = i
    sorted_stations = river_stations[i]
    sorted_stations.sort()

    print(river, sorted_stations)