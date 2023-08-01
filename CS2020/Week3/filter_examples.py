#---------------------------------------------
# CS2020
#
# This illustrates the use of filter function.
# lambda functions are also used here.
# 
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

def isPositive(x):
    return x > 0

def isEven(x):
    return x % 2 == 0

def has5Letters(s):
    return len(s) == 5


L = list(filter(isEven, range(1,11)))

print(L)
print(tuple(L))

L2 =  [-10, 15, -20, 25, -30, 35]

print(list(filter(isPositive, L2)))
print(list(filter(isEven, L2)))

L3 = ["one", "two", "three", "four", "five"]
print(list(filter(has5Letters, L3)))


#Samples using lambda
print(sum(filter(lambda x: x < 0, L2))) 

nestedList = [[10,20,30], [4,5,6], [10,5,5], [20,20]]
print(list(filter(lambda xs : sum(xs) > 20, nestedList)))

