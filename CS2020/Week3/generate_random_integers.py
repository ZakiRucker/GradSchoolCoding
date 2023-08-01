#---------------------------------------------
# CS2020
#
# This illustrates the use of randint from the
# random library to generate random integers.
# 
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

from random import randint 

randList1 = [randint(0,10) for i in range(5)]
print(randList1)

randList2 = [randint(0,i) for i in range(10)]
print(randList2)

randList3 = [randint(i, 100) for i in range(15)]
print(randList3)

