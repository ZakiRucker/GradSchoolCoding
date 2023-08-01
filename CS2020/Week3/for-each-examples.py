#---------------------------------------------
# CS2020
#
# This illustrates the basic use of for-each
# loop.
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------
import math

seq = range(10)

for num in seq:
    val = num * num
    print(num, val)
    
prod = 1
for num in seq:
    prod = prod * num
print(prod)

sum = 0
for cnt in range(1,5) :
    sum += eval(input("Enter No " + str(cnt) + ": "))
print(sum)

sum = 0
for number in [2, 4, 6, 8, 10] :
    sum += number
print(sum)

for val in range(1, 5) :
    print(val, math.cos(val))