#---------------------------------------------
# CS2020
#
# Illustrates the most basic form of function
# definition and function call
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------


def f(x):
    val = x*x + 2*x + 1   # or (x+1) * (x+1)
    return val

x = f(2)
y = f(4)
z = f(7)
w = f(12)

print(x, y, z, w)

