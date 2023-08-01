#---------------------------------------------
# CS2020
#
# This illustrates how sequences can be passed to 
# and return from functions.
# 
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

# maximum of squares of x in seq
def sqrMax(seq):
    val = max(map(lambda x: x * x, seq))
    return val

# max, min, and avg of members in seq as a tuple
def stat(seq):
    mx = max(seq)
    mn = min(seq)
    avg = sum(seq) / len(seq)
    return mx, mn, avg

# return the negatives of seq
def negatives(seq):    
    negs = filter(lambda x: x < 0, seq)
    return negs

## ---------- Sample calls ------------##
print(sqrMax([-4, 5, 8, 10, -20, 5, -3]))
print(stat(range(1,11)))
print(negatives([-4, 5, 8, 10, -20, 5, -3]))