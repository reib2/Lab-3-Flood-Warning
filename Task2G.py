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
stations = stations[:10]

dt = 2

at_risk =[]

for station in stations:
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    p=1
    poly, d0 = polyfit(dates, levels, p)
    slope = np.gradient(poly)
    plot_water_level_with_fit(station, dates, levels, p)
    if slope[1] > 0:
        at_risk.append(station.name)


print(at_risk)