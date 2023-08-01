#---------------------------------------------
# CS2020
#
# Counting the number of words in a given string
#
# This illustrates the use of the split method,
# which makes this problem almost trivial
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

doc = input("Enter sentence: ")

list = doc.split( ) #default delimiter is whitespace, which
                    #is exactly what we want here
                    
print("Doc contains %d words" % len(list))

#may need some improvement as this code counts digits as words, too