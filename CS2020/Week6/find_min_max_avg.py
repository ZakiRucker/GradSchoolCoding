#---------------------------------------------
# CS2900
#
# This illustrates creating a list of 200
# randomly generate integers and finding
# their average, minimum, and maximum. Each integer
# is between -1000 and 1000, inclusive. The function
# randint[a, b] returns a random integer r, such that
# a <= r <= b.
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------
from random import randint
from functools import reduce

def output(min, max, avg):
    print()
    print("%-10s%-10s%-10s" % ("Min:", "Max:", "Avg:"))
    print("%-10d%-10d%-10.3f" % (min, max, avg))
    

##################### Version 1 ##########################    
def version_1():    
    
    xs = []
    for cnt in range(0,200):
        xs += [randint(-1000,1000)]
        
    max = min = xs[0]
    sum = 0.0
    
    for val in xs:
        if max < val: max = val
        elif min > val: min = val
        sum += val
        
    output(min, max, sum/len(xs))
    
##################### Version 2 ##########################  
def version_2():
    
    xs = [randint(-1000,1000) for i in range(0,200)]
    
    output(min(xs), max(xs), sum(xs)/len(xs))
    
    
##################### Version 3 ##########################  
def collect(c, e):
    min, max, sum = c
    if min > e: min =e
    elif max < e: max = e
    sum += e
    return [min, max, sum]
    
def version_3():
    
    xs = list(map(lambda e: randint(-1000,1000), range(0,200)))
    
    (min, max, sum) = reduce(collect,xs, [xs[0],xs[0],0])
    
    output(min, max, sum/len(xs))
    

##------------------ MAIN ------------------##
version_1()
version_2()
version_3()