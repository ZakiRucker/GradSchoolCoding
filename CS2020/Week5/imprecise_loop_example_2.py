#---------------------------------------------
# CS2900
#
# Here's another example of imprecise loop
# control to due to approximation of real
# numbers in computer memory
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

#Loop 1
result, cnt = 0, 0.0

while cnt < 10.0 :
    #print repr(cnt)
    cnt += 1.0
    result += 1

print(result)

#Loop 2
result, cnt = 0, 0.0

while cnt < 1.0 :
    #print repr(cnt)
    cnt += 0.1
    result += 1

print(result)