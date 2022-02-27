import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from floodsystem.stationdata import build_station_list
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def test_polyfit():
    stations = build_station_list()
    two_stations = stations[:2]
    p =4
    dt =2
    for station in two_stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        poly, d0 = polyfit(dates, levels, p)
        assert isinstance(d0, float)
