#---------------------------------------------
# CS2020
#
# This illustrates the use of non-numerical functions.
# Notice the 'hello' function does not include the
# return statement, so it is returning the value None.
# 
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------


def greetings(name):
    return "Hello, " + name + "."

print(greetings("Jack"))
print(greetings("Jill"))
print(greetings("Jane"))
print(greetings("John"))

def hello(name):
    print("Hello, " + name + ".")
    
x = hello("John")
print(x)
print(type(x))