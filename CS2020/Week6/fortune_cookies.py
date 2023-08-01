#---------------------------------------------
# CS2020
#
# Fortune Cookies.
#
# This sample program illustrates the use
# of indexing. Every time you repeat the loop
# it displays randomly selected fortune
#
# Python 2.7
#
# Author: Thomas Otani
# Editor: Zaki Rucker
#---------------------------------------------
from random import randint

fortunes = ["Patience is virtue",
            "Life is short. Enjoy now",
            "You will be rich tomorrow",
            "Your good work will be rewarded",
            "Happiness is earned, never given",
            "Promotion is just around the corner",
            "Work smart, not hard",
            "Don't sweat small stuff"]

limit = len(fortunes)-1

while True:
    reply = raw_input("\nFortune anyone? (yes or no): ")
    
    if reply == "no": break
    
    print("")
    print(fortunes[randint(0,limit)])
    
print("Bye")   
            
