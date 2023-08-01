#---------------------------------------------
# CS2900
#
# This sample program plays arithmetic games
# The user can play as many games as she wants by
# entering Yes to the prompt "Do you want to play game?"
# When No is entered, terminate the program.
#
# At the beginning of each game, the user enters
# N - the number of questions to be asked. Ask the player
# N randomly generated questions and keep
# track of the number correct answers. Each question
# will take the form of
#
#             num1 op num2
#
# where op is + or - and num1 and num2 are
# 1- or 2-digit nonnegative integers (0 to 99). At the conclusion
# of one game, output the number of questions and the number
# of correct answers.
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

#           STEP 1                 #


#Play one game of arithmetic questions
def playOneGame( ) :
    
    print("play one game") #TEMP

#Return True if the answer is Yes to the prompt.
#Return False otherwise
def isReplyYes(prompt) :
    
    response = input(prompt)
    
    if response == "Yes" or response == "yes" :
        return True
    else:
        return False
    
    
    
#############################################
#          main                             #
#############################################

#Play the arithmetic game repeatedly
#until the player wants to quit
prompt = "Play Arithmetics? (Yes or No): "
while isReplyYes(prompt) :
    playOneGame()

print("\nThank you for playing. Good Bye")

    
