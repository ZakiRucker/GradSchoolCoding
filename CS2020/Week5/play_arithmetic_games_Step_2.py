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

#           STEP 2                 #

#Get the number of questions to ask in one game
#Valid number is low to high. Repeat until the valid 
#entry is given
def getQuestionCnt(low, high) :
    
    while True:
        questionCnt = eval(input("How many questions do you want? " + \
                            str(low) + " <= N <= " + str(high) + ": "))
        if low <= questionCnt <= high:
            return questionCnt
        
        print("Invalid entry. Try again")
        
        
#Play one game of arithmetic questions
def playOneGame( ) :
    
    totalQuestion = getQuestionCnt(1, 10)
    correctCnt = 0
    
    for question in range(1, totalQuestion+1) :
        
        answer = 34 #TEMP
        
        reply = eval(input("23 + 11 = ")) #TEMP
        
        if reply == answer:
            correctCnt += 1
            
    print("")
    print("   The game is over.")
    print("# of questions:      %3d" % totalQuestion)
    print("# of correct answers:%3d" % correctCnt)
    print("")
    

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

    
