"""Task 1C: this programme is used to demonstrate the stations_within_radius 
function in the geo.py module."""

#imports
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

stations = build_station_list() #builds list of stations
centre = (52.2053,0.1218) #distance to measure from 
radius = 10

stations_within = stations_within_radius(stations, centre, radius)



print ("The stations within " +str(radius)+"km of "+str(centre) +" are: " +str(stations_within))
