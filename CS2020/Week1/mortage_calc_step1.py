#---------------------------------------------
#
# CS2020 - Mortage Calculator
#          Step 1
#
#          Implement the input routines
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

loanAmount         = input("Loan Amount (Dollars and Cents): ")
annualInterestRate = input("Annual Interest Rate(e.g. 3.5): ")
loanPeriod         = input("Loan Period (in years): ")

# Convert input strings to numerical values
loanAmount         = eval(loanAmount)
annualInterestRate = eval(annualInterestRate)
loanPeriod         = eval(loanPeriod)

# Echo print the input values
print( "\n")
print("Loan Amount:  ", loanAmount)
print("Interest Rate:", annualInterestRate)
print("Loan Period:  ", loanPeriod)