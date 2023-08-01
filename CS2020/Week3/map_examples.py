#---------------------------------------------
# CS2020
#
# This illustrates the use of map function.
# lambda functions are also used here.
# 
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

def double(x):
    return 2 * x

def f(x):
    return x*x + 2*x + 1

L = list(map(double, range(1,11)))

print(L)
print(tuple(L))

print(list(map(f, range(1,11))))
print(list(map(f, L)))


#Samples using lambda
print(sum(map(lambda x: x*x, range(1,6)))) # sum of squares of 1, ..., 5 inclusive

nestedList = [[1,2,3], [4,5,6], [10,10,10,20,20]]
print(max(map(lambda xs : sum(xs), nestedList)))

aList = list(map(lambda x, y: 2*x + y, range(10), range(10)))
bList = list(map(lambda x,y,z: x+y+z, range(10), range(5), range(10)))
print(aList)
print(bList)
