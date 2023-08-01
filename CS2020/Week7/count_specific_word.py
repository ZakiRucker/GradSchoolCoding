#---------------------------------------------
# CS2900
#
# Counting the number of occurrences of a specific
# word in a given string
#
# This illustrates the use of the find method.
# We increment the starting point to the position
# after the previous position the word was found
#
# Note that this is actually a substring search, 
# not exactly finding distinct words. For example,
# word 'is' is found in 'This'. If the sentence
# is "this is it" and word is "is", this will 
# return 2.
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

# Input two strings
doc = raw_input("Enter sentence: ")
word = raw_input("Word to search: ")

start = wordCnt = 0
limit = len(doc)

# if we use the count method then this is all we need to do
# wordCnt = doc.count(word)
# we achieve the same without using the count method

while start < limit:
    loc = doc.find(word, start)
    
    if loc < 0: break
    
    wordCnt += 1
    start = loc + len(word)
    
print("'%s' was found %d times in the document" % (word, wordCnt))
