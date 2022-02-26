import matplotlib.pyplot as plt
import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.station import MonitoringStation

stations = build_station_list()
update_water_levels(stations)
N= 5

five_stations_levels = stations_highest_rel_level(stations, N)
five_stations = []
for i in five_stations_levels:
    five_stations.append(i[0])

print(five_stations)


for station in five_stations:
   
    dt = 10
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))

    plot_water_levels(station, dates, levels)