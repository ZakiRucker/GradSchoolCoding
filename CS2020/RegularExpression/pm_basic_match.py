#--------------------------------
#
# CS 2020 
#
# This program illustrates the basic pattern matching
# techniques with regular expressions. The program
# uses the match method that checks the beginning of the
# string for a match.
#
# Python 3
#
# Author: Thomas Otani
# Edited: Zaki Rucker
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
        choice = raw_input("\nMenu: \n" + \
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
   
         
         
def experimentMatch( ):
    
    pattern = "[A-Z][0-9]+[a-z]" #change pattern to explore PM
    #pattern = "a+b*"
    #pattern = "(a|b)*c+$"
    
    while True:
        inputStr = raw_input("Enter text for " + pattern + " (enter 'exit' to exit): ")
        
        if inputStr == "exit":
            return
        
        # The match method checks the BEGINNING of the inputStr
        # Need to compare the length if you want EXACT match
        # Or put the marker $ at the end of the list. The $ marker
        # matches the end of the string.
        
        if re.match(pattern, inputStr):
            print("Beginning of input matches the pattern")
        else:
            print("Beginning of input DOES NOT match the pattern")
            
            

def matchCS(): 
    
    pattern = "(368|356|389)-[0-9][0-9](1|3)$" # NOTE the $ at the end
    
    while True:
        inputStr = raw_input("Enter text for " + pattern + " (enter 'exit' to exit): ")
        
        if inputStr == "exit":
            return
        
        if re.match(pattern, inputStr):
            print("Valid CS code")
        else:
            print("NOT a valid CS code")
            
    
def matchSSN():
    # put $ at the end of pattern for exact match
    
#    pattern = "[0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]$"
#    pattern = "[0-9]{3}-[0-9]{2}-[0-9]{4}"
    pattern = r"\d\d\d-\d\d-\d\d\d\d$"
    
#    pattern = r"\d{3}-\d{2}-\d{4}$"

    while True:
        inputStr = raw_input("Enter text for " + pattern + " (enter 'exit' to exit): ")
        
        if inputStr == "exit":
            return
        
        if re.match(pattern, inputStr):
            print("Valid SSN Number")
        else:
            print("NOT a valid SSN Number")
    
 
def matchPythonIdentifier( ):

#    pattern = "[_a-zA-Z][_a-zA-Z0-9]*$"
    pattern = r"[_a-zA-Z]\w*$"   
    
    while True:        
        inputStr = raw_input("Enter text for " + pattern + " (enter 'exit' to exit): ")
        
        if inputStr == "exit":
            return
        
        if re.match(pattern, inputStr):
            print("Valid Python Identifier")
        else:
            print("NOT a valid Python Identifier")
            
            
#--------------------------------------------#
#               M A I N                      #
#                                            #
#--------------------------------------------#

while True:
    selection = displayMenu()

    if selection == EXPERIMENT:
        
        experimentMatch()
    
    elif selection == CS:
        
        matchCS()
        
    elif selection == SSN:
        
        matchSSN()
        
    elif selection == PY_IDENT:
        
        matchPythonIdentifier()
        
    else: #QUIT
        break


print("Program shuts down. Good-Bye.")






    
    
