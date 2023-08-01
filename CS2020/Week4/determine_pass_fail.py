#---------------------------------------------
# CS2020
#
# Determine whether the given test score is
# passing or failing score. Score above 70 or more
# is pass.
#
# Input: test score
# Output: designation of pass or fail
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

testScore = eval(input("Test Score: "))

if testScore < 70:
    
    print("You did not pass")
    
else:
    
    print("You pass")