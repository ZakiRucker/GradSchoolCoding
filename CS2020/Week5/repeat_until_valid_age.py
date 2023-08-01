#---------------------------------------------
# CS2900
#
# This illustrates the use of looping structure
# for input validation.
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

# This function accepts two values: lower bound
# and upper bound of an acceptable range. The
# function does not return until a valid input
# is provided
def getAge(low, high) :
    
    prompt = "Enter Age (between " + str(low) + " and " + str(high) + "): "

    age = eval(input(prompt))

    while age < low or age > high :

        print("An invalid age was entered. Please try again.")
    
        age = eval(input(prompt))
        
    return age

#------ main --------------------#
print(getAge(13, 19))   #only teenagers
print(getAge(1, 10))    #age of house you want to buy
print(getAge(100, 200)) #vintage wine 

    