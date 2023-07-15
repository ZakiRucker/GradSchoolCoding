#---------------------------------------------
#
# CS2900 - Compute the height fo the pole
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

from math import *
alphaRad = radians(eval(input("alpha: "))) #enter 24
betaRad  = radians(eval(input("beta: ")))  #enter 23
distance = eval(input("distance: "))       #enter 5000

height = (distance * sin(alphaRad) * sin(betaRad)) / \
         sqrt(sin(alphaRad + betaRad) * sin(alphaRad - betaRad))

print("Height of the pole:", height)
