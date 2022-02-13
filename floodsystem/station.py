# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""
from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import 


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    

    def typical_range_consistent(self):
        """This method checks the typical high/low range data for consistency"""

        range = self.typical_range 
        consistent = True #initiate the consistent variable with True

        if range == None: #check if tuple is empty 
            consistent = False
        elif range[0] > range[1]: #check if the lower value is greater than the higher value
            consistent = False

        return consistent

    def relative_water_level(self):

        range = self.typical_range
        level = self.latest_level

        if self.typical_range_consistent == False:#do we need to call self
            return None      
        else: 

            






        return None
     







def inconsistent_typical_range_stations(stations): 
    """This function returns an alphabetically sorted list of
    stations with inconsistent data for typical range. """

    inconsistent_stations = [] #initiate list to store stations 

    #iterate through stations and call method to check consistency
    for station in stations:
        consistent = station.typical_range_consistent()
        if consistent == False:
            inconsistent_stations.append(station.name)
    
    sorted_list = sorted_by_key(inconsistent_stations, 0) #use sorting module to sort by distance
        
    return sorted_list

