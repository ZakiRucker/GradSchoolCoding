#---------------------------------------------
# CS2020
#
# This illustrates the slicing operation. 
# The list has 20 integers 10, 20, ..., 200. The user
# enters the low and upper index. The program
# terminates when the user enters nothing.
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

L = list(range(10, 210, 10)) #a list whose elements range from 10 to 200
print(L)

print("Enter 'None' (without single quotes; capital N) to stop the repetition")

while True:
    
    low = eval(input("low: "))
    
    if low == None: break
    
    high = eval(input("high: "))
    
    print (L[low:high])
    
print("Bye")