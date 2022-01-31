from haversine import haversine, Unit
    
lyon = (45.7597, 4.8422) # (lat, lon)
paris = (48.8567, 2.3508)

print (haversine(lyon, paris))
 

from utils import sorted_by_key  # noqa
from stationdata import build_station_list


def stations_by_distance(): 
    """This module sorts stations by distance and returns a list of (station, distance) tupules."""
    station = build_station_list()

stations_by_distance()
