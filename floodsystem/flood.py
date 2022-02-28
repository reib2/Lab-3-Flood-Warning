from .station import MonitoringStation
from .utils import sorted_by_key

from floodsystem.datafetcher import fetch_measure_levels
import numpy as np
import datetime
from floodsystem.analysis import polyfit



def stations_level_over_threshold(stations, tol): 
    """This function returns a list of stations where water
    level is above tolerance value."""

    list_stations_over = [] #initiate list to store tuples 

    #iterate through stations and check tolerance 
    for station in stations: 
        fraction = station.relative_water_level() #call function to return relative level fraction
        #print (fraction)
        if fraction != None and fraction > tol:  #check that data consistent and tolerance 
            list_stations_over.append((station.name, fraction)) #append tuple to list 

    sorted_list = sorted_by_key(list_stations_over, 1, True) #sort list descending 

    #print (sorted_list)
    return sorted_list


def stations_highest_rel_level(stations, N):
    """This function returns a list of the most at risk stations."""

    full_station_list = [] #initate list 

    for station in stations:
        fraction = station.relative_water_level() #call function to return relative level fraction
        if fraction != None:  #check that data consistent
            full_station_list.append((station, fraction)) #append tuple to list 
    
    sorted_list = sorted_by_key(full_station_list, 1, True) #sort high to low 

    top_N = sorted_list[:N] #slice list to include top ten entities 

    return top_N



def flood_warning(station_list):
    "Function issues risk level for each station."

    dt = 2
    at_risk =[]
    risk = ""

    for station in station_list:
        #print (station.name)
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt)) #return levels for last two days 

    
        p=1

        try:

            poly, d0 = polyfit(dates, levels, p)

            #print (poly)
            if poly != []: 
                slope = poly[1]

                fraction = station.relative_water_level()

                if slope > 0: #increasing water levels

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

                else: #decreasing water levels
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
        except:
                print (str(station.name) + " Missing data")
                









