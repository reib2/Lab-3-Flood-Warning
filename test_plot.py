from re import L
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def test_plotting():
    station = "test_station"
    dates = [2019, 2020, 2021, 2022]
    levels = [12, 18, 45, 90]
    plt.plot(dates, levels)

    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station)

    assert plt.plot != None
    
