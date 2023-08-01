#---------------------------------------------
# CS2020
#
# Read numbers (float) from the file april_expense.txt
# and compute their sum
#
# Python 3.0
#
# Author: Thomas Otani
#
#-------------------------------------------

file = open("april_expense.txt", "r")

total = 0.0

for line in file:    
    total += float(line)

##------ Using map ---------##    
# file.read() returns the whole file content as
# a single string, then splitlines() converts it
# to a list of strings, one member per line
'''
total = sum(map(float, file.read().splitlines())) 
'''   
    
##------ Using while -------##
'''
total = 0.0

while True:
    line = file.readline()
    
    if line == "":
        break
    
    total += float(line)
'''
##---------------------------##    

    
print("sum =", total)
    
    
    