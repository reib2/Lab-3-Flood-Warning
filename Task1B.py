"""Task 1B: this programme is used to demonstrate the build_station_list 
function in the geo.py module."""

#imports
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

stations = build_station_list() #builds list of stations

p = (52.2053,0.1218) #distance to measure from 

stations_distance = stations_by_distance(stations, p) #returns list of stations sorted by distance 

closest = stations_distance[:10] #slices list to include the 10 locations closest to p 
furthest = stations_distance[-10:] #slices list to include the 10 locations furthest from p 

print ("\nThe ten stations closest to Cambridge City Centre are: " + str(closest))
print ("\n The ten stations furthest from Cambridge City Centre are: " + str(furthest) +"\n ")