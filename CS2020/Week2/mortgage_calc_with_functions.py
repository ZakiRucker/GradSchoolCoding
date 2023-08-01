#---------------------------------------------
#
# CS2020 - Mortage Calculator
#          with functions
#
#          This program uses a number of functions
#          to compute and display mortgage information
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

#Compute the monthly payment given 
#     loan amount          -- dollars and cents
#     annual interest rate -- percent
#     loan period          -- years

def monthlyPayment(amount, rate, period) :
    monthlyRate = rate / 100.0 / 12.0
    paymentCnt = period * 12
    
    payment = (amount * monthlyRate) / \
              (1.0 - (1.0 / (1.0 + monthlyRate)) ** paymentCnt)
    
    return payment


#Compute the total payment given
#     payment amount    -- dollars and cents
#     number of payment -- years

def totalPayment(amountPerPayment, paymentCnt) :
    total = amountPerPayment * paymentCnt * 12  
    return total


#-----------------------------------------------
#        Main Program
#-----------------------------------------------

loanAmount         = eval(input("Loan Amount (Dollars and Cents): "))
annualInterestRate = eval(input("Annual Interest Rate(e.g. 7.5): "))
loanPeriod         = eval(input("Loan Period (in years): "))


#Compute the monthly and total payments
monthlyPayment = monthlyPayment(loanAmount, annualInterestRate, loanPeriod)       
totalPayment   = totalPayment(monthlyPayment, loanPeriod)


# Echo print the input values and display the results
print("\n")
print("Loan Amount:       $%10.2f" % loanAmount)
print("Interest Rate:      %10.2f%%" % annualInterestRate) #use %% to output %
print("Loan Period:        %10d years" % loanPeriod)

print("")
print("Monthly payment is $%10.2f" % monthlyPayment)
print("  TOTAL payment is $%10.2f" % totalPayment)

