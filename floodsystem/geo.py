# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit #import haversine function from library
from floodsystem.utils import sorted_by_key


def stations_by_distance(stations, p): 
    """This module sorts stations by distance and returns a 
    list of (station, town, distance) tupules."""

    list_station_dist = [] #initiates list to store stations and distance 
      
    #iterate through stations and calculate distamces
    for station in stations:
        distance = haversine(station.coord, p) #use haversine function to calculate distance between station and p  
        list_station_dist.append((station.name, station.town, distance)) #add data to list
    
    sorted_list = sorted_by_key(list_station_dist, 2) #use sorting module to sort by distance

    return sorted_list 



def stations_within_radius(stations, centre, r): 
   
    list_within_radius = []

    for station in stations:
        distance = haversine(station.coord, centre)
        if distance < r: 
            list_within_radius.append(station.name)

    sorted_list = sorted_by_key(list_within_radius, 0)

    return sorted_list



