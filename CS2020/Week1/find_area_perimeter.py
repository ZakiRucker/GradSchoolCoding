"""
#---------------------------------------------
# CS2020 - Compute the area and the perimeter
#          of a rectangular plot
# Python 3.0
# Author: Thomas Otani
#---------------------------------------------
"""

#Input the width and the length of a rectangular plot
width  = input('Width (ft): ')
length = input('Length (ft): ')

width  = eval(width)
length = eval(length)

#Compute the area and the perimeter
area = width * length
perimeter = 2 * width + 2 * length

#Echo the input values and display the results
print(" ")
print("Width     =", width)
print("Length    =", length)
print("Area      =", area)
print("Perimeter =", perimeter)
