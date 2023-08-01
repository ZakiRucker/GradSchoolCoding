#---------------------------------------------
# CS2020
#
# Illustrates the nested function calls
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

def sum(x, y) :     # Notice that x and y are local to this function.
    s = x + y 
    return s        # They are different from other x's and y's

def prod(x, y) :
    p = x * y
    return p

def poly(x) :       #compute x**2 + 2*x + 1
    result = prod(x,x) + sum(x,x) + 1
    return result


############ Main ################

print(poly(1.0))
print(poly(3.5))
print(poly(-1.0))