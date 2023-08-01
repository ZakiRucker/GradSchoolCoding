#---------------------------------------------
# CS2900
#
# This illustrates the use of break and continue
# statements in the loop control
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

#Compute the sum of N positive integers
#Abort the whole process if a negative number is entered
def computeSumOfNPos(N) :
    
    cnt = sum = 0
    print("Enter", N, "numbers")
    
    while cnt < N :
        
        number = eval(input())
        
        if number < 0: #negative number is entered,
            sum = -1   #signal an error and
            break      #break out from this loop completely
        
        sum += number
        cnt += 1
        
    return sum


#Compute the sum of N positive integers
#Exclude any negative integers
def computeSumOfNPosVersion2(N) :
    
    cnt = sum = 0
    print("Enter", N, "numbers")
    1
    while cnt < N :
        
        number = eval(input())
        
        if number < 0:   #ignore a negative number
            continue     #by skipping the remain code in the loop
        
        sum += number
        cnt += 1
        
    return sum


############## main ############################

sum = computeSumOfNPos(5)
if (sum < 0) :
    print("Error: negative number is entered")
else:
    print("sum", sum)
    
sum = computeSumOfNPosVersion2(5)
print("sum", sum)
