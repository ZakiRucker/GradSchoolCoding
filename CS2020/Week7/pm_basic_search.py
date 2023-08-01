#--------------------------------
#
# CS 2020 
#
# This program illustrates the basic pattern matching
# techniques with regular expressions This program
# uses the search method that locates a pattern 
# in a given string.
#
# Python 3
#
# Author: Thomas Otani
#--------------------------------

import re


EXPERIMENT = "E"
CS = "B"
SSN = "S"
PY_IDENT = "I"
QUIT = "Q"

MENU_SELECTION = [EXPERIMENT, CS, SSN, PY_IDENT, QUIT]
    
#Display menu choices and
#return the selection to the caller
def displayMenu( ):
    
    while True:
        choice = input("\nMenu: \n" + \
                       "   Experiment ---> " + EXPERIMENT + "\n" + \
                       "   CS Code    ---> " + CS         + "\n" + \
                       "   SSN        ---> " + SSN        + "\n" + \
                       "   Identifier ---> " + PY_IDENT   + "\n" + \
                       " ------------------------\n"        + \
                       "   Quit       ---> " + QUIT + "\n")
        
        choice = choice.upper()
        
        if choice in MENU_SELECTION:
            return choice        
        else:
            print("Error: Invalid selection. Try again.\n")
   
         
         
def experimentSearch( ):
    
    pattern = "[A-Z][0-9]+[a-z]" #change pattern to explore PM
    #pattern = a+b*
    #pattern = (a|b)*c+$
    
    while True:
        inputStr = input("Enter text for " + pattern + " (enter 'exit' to exit): ")
        
        if inputStr == "exit":
            return
        
        # The search method looks for an occurrence of a pattern
        # in the string.
        
        if re.search(pattern, inputStr):
            print("The pattern appears in the string")
        else:
            print("The pattern DOES NOT appear the pattern")
            
            

def searchCS(): 
    
    pattern = "(368|356|389)-[0-9][0-9](1|3)" 
    
    while True:
        inputStr = input("Enter text for " + pattern + " (enter 'exit' to exit): ")
        
        if inputStr == "exit":
            return
        
        if re.search(pattern, inputStr):
            print("Valid CS code appears in the string")
        else:
            print("A valid CS code is not found in the string")
            
    
def searchSSN():
    # put $ at the end of pattern for exact match
    
#    pattern = "[0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]"
#    pattern = "[0-9]{3}-[0-9]{2}-[0-9]{4}"
    pattern = r"\d\d\d-\d\d-\d\d\d\d"
#    pattern = r"\d{3}-\d{2}-\d{4}"

    while True:
        inputStr = input("Enter text for " + pattern + " (enter 'exit' to exit): ")
        
        if inputStr == "exit":
            return
        
        if re.search(pattern, inputStr):
            print("Valid SSN Number found in the string")
        else:
            print("NOT a valid SSN Number found in the string")
    
 
def searchPythonIdentifier( ):

#    pattern = "[_a-zA-Z][_a-zA-Z0-9]*"
    pattern = r"[_a-zA-Z]\w*"   
    
    while True:        
        inputStr = input("Enter text for " + pattern + " (enter 'exit' to exit): ")
        
        if inputStr == "exit":
            return
        
        if re.search(pattern, inputStr):
            print("Valid Python Identifier appears in the string")
        else:
            print("A valid Python Identifier does not appear in the string")
            
            
#--------------------------------------------#
#               M A I N                      #
#                                            #
#--------------------------------------------#

while True:
    selection = displayMenu()

    if selection == EXPERIMENT:
        
        experimentSearch()
    
    elif selection == CS:
        
        searchCS()
        
    elif selection == SSN:
        
        searchSSN()
        
    elif selection == PY_IDENT:
        
        searchPythonIdentifier()
        
    else: #QUIT
        break


print("Program shuts down. Good-Bye.")






    
    
