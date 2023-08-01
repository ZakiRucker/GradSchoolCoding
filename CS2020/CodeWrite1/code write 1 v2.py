#print "Hello, Zaki"
#if isAgeValid(age) and isHeightValid(height) :
    
#    recommendWgt = getRecommendWgt(age, height)
    
#    print("Recommended Wgt for %d-year-old %dcm person is %1.1fkg" % \
           #(age, height, recommendWgt))
    
#else:
    
#    print("Program Aborted: Invalid Input")

#for i in range(1, 11):
#   format = "%"+ str(11-i) + "s"
#   print(format % "*")



def Z(x, y) :     # Notice that x and y are local to this function.
    Z = Z*X
    return Z

x = input("Enter a positive integer:")

if x == 0:
    ZEQ = str("undefined, please enter a positive integer greater than zero.")

elif x == 1:
    ZEQ = x

while x >1:
    Z = Z * x
    x -= 1
    print x
    print Z

print Z
