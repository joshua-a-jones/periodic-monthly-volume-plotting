#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 30 2021

@author: joshuajones
"""

import numpy as np
import matplotlib.pyplot as plt
from production_functions import exponential_equation, hyperbolic_equation, harmonic_equation, periodic_monthly_volume


# create time vector for calculations. 40 years X 12 months + 1 month. 
# The +1 is because we have 480 months, but we run from start of first month to end of final month
t = np.float64(range(0,40*12+1))

## define initial conditions for exponential curve
# units for Qi are converted to Mcf per month
# units for Di are converted to 1/month
Qi_exponential = 5000.0*365/12
Di_exponential = 2.0/12

pmv_exponential = periodic_monthly_volume(exponential_equation(t, Qi_exponential, Di_exponential))

## define initial conditions for hyperbolic curve
# units for Qi are converted to Mcf per month
# units for Di are converted to 1/month
Qi_hyperbolic = 15000*365/12
Di_hyperbolic = 1.4/12
B_hyperbolic = 1.5
Dmin_hyperbolic = 0.06/12

pmv_hyperbolic = periodic_monthly_volume(hyperbolic_equation(t, Qi_hyperbolic, B_hyperbolic, Di_hyperbolic, Dmin_hyperbolic))

## define initial conditions for harmonic curve
# units for Qi are converted to Mcf per month
# units for Di are converted to 1/month
Qi_harmonic = 10000*365/12
Di_harmonic = 1.2/12
Dmin_harmonic = 0.10/12

pmv_harmonic = periodic_monthly_volume(harmonic_equation(t, Qi_harmonic, Di_harmonic, Dmin_harmonic))



# Create plots. t runs from 0 to 481. We only have 480 months to plot, so drop last value of t
plt.semilogy(t[0:-1],pmv_exponential)
plt.semilogy(t[0:-1],pmv_hyperbolic)
plt.semilogy(t[0:-1],pmv_harmonic)

# make the plots pretty with axis labels and a legend
plt.xlim(xmin=0, xmax = 480)
plt.ylim(ymin = 1)
plt.title('Periodic Monthly Volumes Comparison')
plt.ylabel('Periodic Monthly Volume (Mcf)')
plt.xlabel('Months Since Start')
plt.legend(['Exponential','Hyperbolic','Harmonic'])
plt.grid(True, which = 'both')










