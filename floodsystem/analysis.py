import matplotlib
import numpy as np
import matplotlib.pyplot as plt

def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    y = levels
    p_coeff = np.polyfit(x - x[0], y, p)
    poly = np.poly1d(p_coeff)

    d0 = matplotlib.dates.date2num(dates[0])

    return poly, d0
