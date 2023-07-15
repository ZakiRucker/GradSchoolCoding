#---------------------------------------------
#
# CS2020 - Mortage Calculator
#          Step 2
#
#          Implement the output routines
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

#Compute the monthly and total payments
monthlyPayment = 143.47  #TO DO - replace with the real one
totalPayment = 17216.50  #TO DO - replace with the real one

# Echo print the input values and display the results
print("\n")
print("Loan Amount:           $", loanAmount)
print("Interest Rate:          ", annualInterestRate, "%")
print("Loan Period (years):    ", loanPeriod)

print("")
print("Monthly payment is     $", monthlyPayment)
print("  TOTAL payment is     $", totalPayment)