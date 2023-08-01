#---------------------------------------------
# CS2020
#
# Determine whether the given test score is
# passing or failing score. Input also include age. 
# Score above 70 or more is pass. Additional message
# displayed for those less than 10.
#
# Input: test score
# Output: designation of pass or fail
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

testScore  = eval(input("Test Score: "))
studentAge = eval(input("Your age: "))

if testScore >= 70:
    if studentAge < 10:
        print("You did a great job")
    else:
        print("You did pass") # test score >= 70 and age >= 10
        
else: # test score < 70
    print("You did not pass")