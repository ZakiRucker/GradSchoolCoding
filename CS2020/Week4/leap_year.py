#---------------------------------------------
# CS2900
#
# Determine if the given year is a leap year or not
# 
# It is a leap year if the year is
#    1. divisible by 4 but not by 100 (1796 is leap, but 1800 is not)
#          (divisible by 100 is a century year 1600, 1700, 1800, etc)
#    2. divisible by both 4 and 100 and also by 400 (2000 is leap)
# 
# E.g. 1800, 1900, 2100, 2300, and 2500 are NOT leap. 2000 and 2400 are leap
#
# See http://www.timeanddate.com/date/leapyear.html for details
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

year = eval(input("Enter year (YYYY): "))

#Approach 1 - Using if/elif
if year % 4 != 0 :  # not divisible by 4
    
    result = "NOT Leap"
    
elif year % 100 !=0 :   # div by 4, not div by 100
    
    result = "Leap"
    
elif year % 400 == 0 :  # div by 4, div by 100, div by 400
    
    result = "Leap"
    
else: #div by 4, div by 100, not div by 400
    
    result = "NOT Leap"
    
print(result)

#Approach 2 - Using nested if equivalent of Approach 1
#             Note that the nested else blocks have further if's
if year % 4 != 0 :  # not divisible by 4
    
    result = "NOT Leap"
    
else:
    if year % 100 !=0 :   # div by 4, not div by 100
    
        result = "Leap"
    
    else:
        
        if year % 400 == 0 :  # div by 4, div by 100, div by 400
    
            result = "Leap"
    
        else: #div by 4, div by 100, not div by 400
    
            result = "NOT Leap"
    
print(result)

#Approach 3 - Using nested if; variation of Approach 2, switching <then>
#             and <else> of nested part. You cannot translate this back
#             to if/elif stucture directly because the <then> block is 
#             is nested here
if year % 4 != 0 :  # not divisible by 4
    
    result = "NOT Leap"
    
else:
    if year % 100 ==0 :   # div by 4, div by 100
    
        if year % 400 == 0 :  # div by 4, div by 100, div by 400
    
            result = "Leap"
    
        else: #div by 4, div by 100, not div by 400
    
            result = "NOT Leap"
    
    else: #div by 4, not div by 100
        
        result = "Leap"
           
print(result)

#Approach 4 - No nestings; using logical operators 'and' and 'or' 
#             Parentheses are actually not necessary here because 
#             'and' has a higher precedence than 'or'
if (year % 4 == 0 and year % 100 != 0) or \
   (year % 4 == 0 and year % 100 == 0 and year % 400 == 0) :
     
    result = "Leap"
    
else:
    
    result = "NOT Leap"

print(result)


#Approach 5 - No nestings; negated form of Approach 4
if not (year % 4 == 0 and year % 100 != 0) and \
   not (year % 4 == 0 and year % 100 == 0 and year % 400 == 0) :
    
    result = "NOT Leap"
    
else:
    
    result = "Leap"
    
print(result)

#Approach 6 - Negation distributed using De Morgan's Law
if (year % 4 != 0 or year % 100 == 0) and \
   (year % 4 != 0 or year % 100 != 0 or year % 400 != 0) :
    
    result = "NOT Leap"
    
else:
    
    result = "Leap"
    
print(result)

#Approach 7 - Use the fact that if Y is divisible by 400, then
#             Y is also divisible by 4. 
if (year % 400 == 0) or \
   (year % 4 == 0 and year % 100 != 0) :
    
    result = "Leap"
    
else:
    
    result = "NOT Leap"
    
print(result)