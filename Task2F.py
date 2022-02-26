import matplotlib.pyplot as plt
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
import matplotlib
import numpy as np
import datetime
from floodsystem.plot import plot_water_levels, plot_water_level_with_fit
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.station import MonitoringStation
from floodsystem.analysis import polyfit

stations = build_station_list()
update_water_levels(stations)
N= 6

five_stations_levels = stations_highest_rel_level(stations, N)
five_stations = []
for i in five_stations_levels:
    five_stations.append(i[0])

del five_stations[0]
print(five_stations)
for station in five_stations:
   
    dt = 10
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))

    p=4

    plot_water_level_with_fit(station, dates, levels, p)