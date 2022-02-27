import matplotlib.pyplot as plt
from floodsystem.flood import stations_level_over_threshold
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


#build list and splice
stations = build_station_list() 
update_water_levels(stations)
stations = stations[:40]


dt = 2
at_risk =[]
risk = ""

for station in stations:
    #print (station.name)
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    p=1

    poly, d0 = polyfit(dates, levels, p)

    #print (poly)
    if poly != None: 
        slope = poly[1]

        fraction = station.relative_water_level()

        if slope > 0:

            if fraction != None: 
                if fraction < 0.8:
                    risk = "LOW"
                elif fraction < 1: 
                    risk = "MODERATE"
                elif fraction < 1.5:
                    risk = "HIGH"
                else: 
                    risk = "SEVERE"
            
            print (str(station.name) + " " + str(risk)) 

            #at_risk.append((station.name, risk))

        else:
            if fraction != None: 
                if fraction < 1:
                    risk = "LOW"
                elif fraction < 2: 
                    risk = "MODERATE"
                elif fraction < 5:
                    risk = "HIGH"
                else: 
                    risk = "SEVERE"

            print (str(station.name) + " " + str(risk))
            #at_risk.append((station.name, risk))
        
        

