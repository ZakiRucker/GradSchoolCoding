#---------------------------------------------
# CS2020
#
# Counting the number of words in a given string
#
# Same as count_words.py but this one does it
# without creating a list
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

doc = input("Enter sentence: ")

doc = doc.strip() #remove leading and trailing whitespace

limit = len(doc)

idx = wordCnt = 0

while idx < limit:
    
    #look for the start of a word
    while idx < limit:
        if not doc[idx].isspace():
            break
        idx += 1
        
    #now look for the end of the word
    while idx < limit:
        if doc[idx].isspace(): 
            wordCnt += 1
            break
        idx += 1
    else: #handles the last word, there's no space after the last word
        wordCnt += 1 
                    
print("Doc contains %d words" % wordCnt)

#may need some improvement as this code counts digits as words, too