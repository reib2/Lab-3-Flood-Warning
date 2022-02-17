from .station import MonitoringStation
from .utils import sorted_by_key


def stations_level_over_threshold(stations, tol): 
    """This function returns a list of stations where water
    level is above tolerance value."""

    list_stations_over = [] #initiate list to store tuples 

    #iterate through stations and check tolerance 
    for station in stations: 
        fraction = station.relative_water_level() #call function to return relative level fraction

        if fraction != None and fraction > tol:  #check that data consistent and tolerance 
            list_stations_over.append((station.name, fraction)) #append tuple to list 

    sorted_list = sorted_by_key(list_stations_over, 1, True) #sort list descending 

    return sorted_list


