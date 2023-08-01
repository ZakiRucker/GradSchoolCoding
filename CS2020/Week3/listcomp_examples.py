#---------------------------------------------
# CS2020
#
# This illustrates the list comprehension operation.
# 
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------


L = [33, -998, 22, -10, 34, 77, 43]

squares = [x*x for x in L]
evens = [x for x in range(30) if x % 2 == 0]
negatives = [2 * x for x in L if x < 0]

print(squares)
print(evens)
print(negatives)
