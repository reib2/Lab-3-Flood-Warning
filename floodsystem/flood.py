from .station import MonitoringStation
from .utils import sorted_by_key


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
            full_station_list.append((station.name, fraction)) #append tuple to list 
    
    sorted_list = sorted_by_key(full_station_list, 1, True) #sort high to low 

    top_ten = sorted_list[:N] #slice list to include top ten entities 

    return top_ten











