from floodsystem.station import MonitoringStation

def stations_level_over_threshold(stations, tol): 
    for station in stations: 
        fraction = station.relative_water_level

        print (fraction)


    

