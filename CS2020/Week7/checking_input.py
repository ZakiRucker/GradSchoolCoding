#---------------------------------------------
# CS2020
#
# This illustrates an input type checking using
# string processing technique.
#
# Code for checking input real number has a bug.
# It will give false positive, i.e., it will say
# input is valid when it is not for certain types
# of input. What is it? And how do you fix it?
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

#Notice we are not applying the eval function
#We receive input as a string
val = raw_input("Enter integer: ")

if val.isdigit() :
    print("input okay")
else:
    print("Invalid: nondigit character")
    
#The following code has a bug. Can you find it?
val = raw_input("Enter real number: ") #this code has a bug

for ch in val:
 if not ch.isdigit() and ch != "." :
    print("Error"); break
 else:
    print("Input valid")
