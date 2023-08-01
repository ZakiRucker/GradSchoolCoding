#---------------------------------------------
# CS2900
#
# This illustrates the basic for-each loop
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------
from random import randint

'''
Count how many times val occurs in list xs
'''
def myCount(xs, val):
    cnt = 0
    
    for x in xs:
        if x == val: cnt += 1
        
    return cnt

'''
Compute the sum of all members of number list xs
'''
def mySum(xs):
    total = 0
    
    for x in xs:
        total += x
        
    return total

'''
Compute the size (length) of list xs
'''
def myLen(s):
    cnt = 0
    
    for x in xs:
        cnt += 1
        
    return cnt

'''
Find the maximum member in list xs
xs must nonempty
'''
def myMax(xs):
    max = xs[0]
    
    for x in xs:
        if max > x: max = x
    
    return max

'''
Find the minimum member in list xs
'''
def myMin(xs):
    min = xs[0]
    
    for x in xs:
        if min < x: min = x
    
    return max

'''
Find the position of　val in list xs
'''
def myIndex(xs, val):
    loc = 0
    
    for x in xs:
        if x == val: return loc
        loc += 1
        
    return loc


'''
Find all positions of val in list xs.
Return the result as a list
'''
def allIndices(xs, val):
    result = []
    
    for x in xs:
        if x == val: result += [x]
    
    return result


###------------------------------------------###
# ------------  Test Runs ------------------- #
print("Start Tests")

L = [randint(0,100) for i in range(2000)]

smallest = myMin(L)
assert(smallest, min(L))

largest = myMax(L)
assert(largest, max(L))



print("End Tests")

