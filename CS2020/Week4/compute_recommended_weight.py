#---------------------------------------------
# CS2020
#
# Compute a person's recommended weight given
# the person's age and height (cm). the formula
# is
#    recommended wgt = (ht - 100 + age / 10.0) * 0.90
#
# We restrict to age between 10 and 100 inclusive and
# height between 50 and 220 cm, inclusive. Invalid
# entry will result in an error message
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

def isAgeValid(age) :
    return 10 <= age <= 100

def isHeightValid(height) :
    return 50 <= height <= 220

def getRecommendWgt(age, height) :
    return (height - 100 + age/10.0) * 0.9

#----------- main -----------#
age = eval(input("Enter age: "))
height = eval(input("Enter height (in cm): "))

if isAgeValid(age) and isHeightValid(height) :
    
    recommendWgt = getRecommendWgt(age, height)
    
    print("Recommended Wgt for %d-year-old %dcm person is %4.1fkg" % \
           (age, height, recommendWgt))
    
else:
    
    print("Program Aborted: Invalid Input")

