#---------------------------------------------
#
# CS2020 - Mortage Calculator
#          Step 3
#
#          Implement the computation rourtine
#          to calculate the monthly and total
#          payments
#
#          M = (L * R) / 1 - (1 / (1+R)) ** N
#
#          M - monthly payment; L - loan amount
#          R - monthly rate; N - number of payments
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

# Compute the monthly and total payments
monthlyRate = annualInterestRate / 100.0 / 12.0
paymentCnt = loanPeriod * 12

# For a multi-line statement use backslach \ to continue 
monthlyPayment = (loanAmount * monthlyRate) / \
                 (1.0 - (1.0 / (1.0 + monthlyRate)) ** paymentCnt)
                 
totalPayment = monthlyPayment * paymentCnt

# Display the results
print("\n")
print("Loan Amount:           $", loanAmount)
print("Interest Rate:          ", annualInterestRate, "%")
print("Loan Period (years):    ", loanPeriod)

print("")
print("Monthly payment is     $", monthlyPayment)
print("  TOTAL payment is     $", totalPayment)