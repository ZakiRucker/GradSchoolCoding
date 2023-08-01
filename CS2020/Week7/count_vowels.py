#---------------------------------------------
# CS2020
#
# Counting Vowels a, e, i, o, u
#
# This illustrates the scanning the characters
# in a string and checking if they are vowels.
# The program counts the number of vowels in
# the string
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------
def isVowel(ch):
    ch = ch.upper()
    
    return ch in "AEIOU"

    '''
    return ch == "A" or ch == "E" or ch == "I" or \
           ch == "O" or ch == "U" :
    '''

    
#----------- main -----------------#
doc = raw_input("Enter sentence: ")

#Approach 1
vowelCnt = 0

for ch in doc:
    if isVowel(ch): vowelCnt += 1
    
print("There are %d vowels" % vowelCnt)

#Approach 2
vowelCnt = len(list(filter(isVowel,doc)))

print("There are %d vowels" % vowelCnt)

