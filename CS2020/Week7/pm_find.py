#--------------------------------
#
# CS 2020 
#
# This program illustrates the use of findall and finditer methods
# of the re module
#
# Python 3
#
# Author: Thomas Otani
#--------------------------------
import re

def getFile( ):
    filename = input("Enter the name of a file to process: ")
    file = open(filename, "r")
    return file

def getPattern( ):
    
    s = input("\nEnter the pattern to search for: ")
    return s


##--------------- M A I N ----------------------##

file = getFile( )
data = file.read();

while True:
    
    pattern = getPattern( )
    
    if pattern == "quit" : break
    
    # findall returns a list of strings that matched the pattern
    result = re.findall(pattern, data)
    
    for item in result:
        print(item)
      
        
    # finditer returns a list of Match objects that matched the pattern
    result = re.finditer(pattern, data)
    
    for match in result:
        print(match.string[match.start(): match.end()], match.start(), match.end())
        
print("Good Bye")