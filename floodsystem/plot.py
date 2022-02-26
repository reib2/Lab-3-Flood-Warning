import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list


def plot_water_levels(station, dates, levels):
    
     plt.plot(dates,levels)

     lower_range = station.typical_range[0]
     higher_range = station.typical_range[1]

     higher = []
     lower = []

     for i in range (len(dates)):
          higher.append(higher_range)
          lower.append(lower_range)

     plt.plot(dates, higher)
     plt.plot(dates, lower)
    
     plt.xlabel('date')
     plt.ylabel('water level (m)')
     plt.xticks(rotation=45);
     plt.title(station.name)
    
     plt.tight_layout()
    
     plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
     