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
    """This module returns a list of stations within a given 
    radius of a coordinat."""
   
    list_within_radius = [] #initiates list to store station names

    #iterate through stations and check if within radius 
    for station in stations:
        distance = haversine(station.coord, centre)
        if distance < r: 
            list_within_radius.append(station.name)

    sorted_list = sorted_by_key(list_within_radius, 0) #use sorting module to sort by distance

    return sorted_list



def rivers_with_station(stations):
    "This module returns a set with the names of rivers with moitoring stations given a list of station objects"


def stations_by_river(stations):
    "This module returns a dictionary that maps river names to a list of station objects on a given river"

def rivers_by_station_number(stations, N):
    "This module returns a list of tuples sorted by the number os stations"
