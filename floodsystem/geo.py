# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from floodsystem.stationdata import build_station_list



def stations_by_distance(stations, p): 
    """This module sorts stations by distance and returns a list of (station, distance) tupules."""
    from haversine import haversine, Unit
 

    # Print number of stations
    print("Number of stations: {}".format(len(stations)))

    # Display data from 3 stations:
    for station in stations:
        if station.name in ['Cambridge Jesus Lock']:
            coord = station.coord
            distance = haversine(coord, p)
            print (distance)


    #print (haversine(lyon, paris))


