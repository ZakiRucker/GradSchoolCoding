#---------------------------------------------
#
# CS2020 - Mortage Calculator
#          Step 4
#
#          Format the output to align values
#          properly
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

# Display the formatted results
print("\n")
print("Loan Amount:       $%10.2f" % loanAmount)
print("Interest Rate:      %10.2f%%" % annualInterestRate) #use %% to output %
print("Loan Period:        %10d years" % loanPeriod)

print("")
print("Monthly payment is $%10.2f" % monthlyPayment)
print("  TOTAL payment is $%10.2f" % totalPayment)