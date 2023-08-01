#---------------------------------------------
# CS2020
#
# Baristas at MoonDeer Coffee earn the basic
# hourly wage of $9.95. They receive time-and-a-half
# of their basic rate for overtime hours (those
# over 40 hours). In addition, they receive a 
# commission on the sales they generate while
# tending the espresso machine. The commission is
# based on the following formula:
#
#    Sales Volume         Commission
#    $100.00 to $299.99    5% of sales
#    $300.00 to $499.00   10% of sales
#    >= $500.00           15% of sales
#
# Input: Sales Volume and Hours worked
# Output: Wage
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

def salary(hours) :
    
    if hours <= 40:
        pay = hours * 9.95
        
    else:
        pay = 9.95 * 40.0 + (1.5 * 9.95) * (hours - 40)
        
    return pay


def commission(sales) :
    
    if sales >= 400:
        comm = sales * 0.15
        
    elif sales >= 300:
        comm = sales * 0.10
        
    elif sales >= 100:
        comm = sales * 0.05
        
    else:
        comm = 0.0
        
    return comm

    
sales = eval(input("Enter Sales Volume: "))
hours = eval(input("Enter Hours Worked: "))

wage = salary(hours) + commission(sales)

print("\n\n")
print("Sales Volume: $%7.2f" % sales)
print("Hours Worked:  %7d hours" % hours)
print("----------------------")
print("Total Wage:   $%7.2f" % wage)