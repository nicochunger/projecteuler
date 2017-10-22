# -*- coding: utf-8 -*-
# Time equation for egg boiling

from math import log, pi, floor

c = 3.7 # Calor especifico
rho = 1.038 # Densidad
K = 5.4e-3 # Conductividad termica

def egg_time(M, To, Tw, Ty):
    p1 = M**(2.0/3)*c*rho**(1.0/3)
    p2 = K*pi**2*(4*pi/3)**(2.0/3)
    p3 = log(0.76*float(To-Tw)/(Ty-Tw))
    return p1*p3/p2

M = 55 # Mass of egg
To = 7.3 # Temperature of egg
Tw = 100 # Temperature of water
Ty = 80 # Goal temperature
time = egg_time(M, To, Tw, Ty)
time_min = floor(time/60)
time_seg = time%60
print "The time to cook a %gg egg at %gC until it reaches \
an internal temperature of %gC is: %d minutes, %d seconds" % (M, To, Ty, time_min, time_seg)
