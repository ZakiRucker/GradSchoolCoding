#---------------------------------------------------------
#
# CS2020
#
# Python Parameter Passing Illustrated
# 
# This program illustrates the call-by-value parameter
# passing. The values of the arguments are passed to
# the corresponding parameters. Changes made to the
# parameters do not affect the arguments.
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------------------

def swap(x, y) :
    print("")
    print("\tBEFORE SWAP: x=", x, "y=", y)
    
    x, y = y, x #swaps the values of x and y
                #but this swap is not reflected in the corresponding arguments
                
    print("\tAFTER SWAP:  x=", x, "y=", y)
    print("")

#------------- MAIN --------------------#                
a = 10
b = 20

print("BEFORE Calling SWAP: a=", a, "b=", b)

swap(a, b)

print("AFTER CallingS WAP:  a=", a, "b=", b)
    
    