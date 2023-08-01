#---------------------------------------------
# CS2020
#
# California Big Lotto.
#
# This illustrates the use of 'in' operator
#
# The program generates a list of five numbers,
# each number drawn from 1 to 47. The user enters
# five numbers from 1 to 47. If all five numbers
# match, you get an A in class.
#
# Warning: This sample program is not an endorsement for
#          gambling.
#
# Python 2.7
#
# Author: Thomas Otani
# Edited: Zaki Rucker
#---------------------------------------------
"""I have added a link in Python books on Python dictionary.
You can use any source of learning from the web,
and understand the basics of a dictionary.
You have to change the BigLotto code to use a dictionary.
Specifically the function DisplayResult."""

from random import randint

#Spin the Big Wheel
#return a list of five integers ranging from 1 to 47
def spinBigWheel( ):
    
    done = False
    list = []
    
    while not done:
        number = randint(1, 47)
        
        if number not in list: #not a duplicate so add it
            list += [number]   #or list.append(number)
            
            if len(list) == 5: 
                done = True
    
    return list

#Get five numbers from the user
#Do not accept any duplicate values
def buyTicket( ):
    
    done = False
    list = []
    
    while not done:
        number = eval(raw_input("Enter 1 <= number <= 47: "))
        
        if number == None: return
        
        if number < 1 or number > 47 or number in list:
            print("Invalid entry")
        
        else:
            list += [number]
            
            if len(list) == 5:
                done = True
            
    return list

"""    
#Display the result
def displayResult(matchCnt):
    
    if matchCnt == 5:
        print("You won $100,000 and an A in CS2020")
    elif matchCnt == 4:
        print("You won $500")
    elif matchCnt == 3:
        print("You won $25")
    elif matchCnt == 2:
        print("You won $1")
    else:
        print("Better luck next time")
"""

dis = {5: "You won $100,000 and on A in CS2020",
          4: "You won $500",
          3: "You won $25",
          2: "You won $1",
          1: "Better luck next time",
          0: "Better luck next time"
          }
#print dis 

      
        
#------------- main -------------------#

while True:
    
    winningNumbers = spinBigWheel()
    
    ticket = buyTicket()
    
    if ticket == None: break
    
    matchCnt = 0
    for val in ticket:
        if val in winningNumbers:
            matchCnt += 1
    
 #   print("Winning Numbers = ", winningNumbers)
    
 #   displayResult(matchCnt)
    print dis [matchCnt]
    
    
