#---------------------------------------------
# CS2900
#
# This illustrates the danger of using
# real number (float) as a counter variable
# due to the imprecision in storing
# real numbers in computer memory
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

count = 0.0

#This loop will stop
#There are sixteen 3s
#Uncomment the print statement and change the boolean expression
# 
#       count != 1.0 
# to
#        count <= 1.0 
# 
# Check the values printed out. Is the third value equals 1.0?
while count != 1.0 :
    count += 0.3333333333333333   
    #print("%20.18f" % count)

print()

count = 0.0
#This loop does not stop, an infinite loop
#There are fifteen 3s
#Uncomment the print statement and change the boolean expression
# 
#       count != 1.0 
# to
#        count <= 1.0 
# 
# Check the values printed out. Is the third value equals 1.0?
while count != 1.0 :
    count += 0.333333333333333
    #print("%20.18f" % count)
        



