#---------------------------------------------
# CS2020
#
# List Memory Allocation.
#
# This shows how a list is allocated in the
# special memory space called heap. The list
# variable contains the address of where the
# list is stored in the heap.
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------


#inplace change; x and y point to the same list
x = [10, 20]
y = x
x.append(30)
print(y)  #outputs [10, 20, 30]

print(id(x)) #this print outs the address of the list referenced by x
print(id(y))
print("")

#concatenation; x is reset to point to a different list
x = [10, 20]
y = x
x = x + [30]
print(y)       #outputs [10, 20]

print(id(x))
print(id(y))
print("")

#WHAT? Shortcut operator x += [30] is NOT equivalent to x = x + [30]
x = [10, 20]
y = x
x += [30]    #same effect as x.append(30)
print(y)     #outputs [10, 20, 30], not [10, 20]

print(id(x))
print(id(y))