'''
13. Using while, input integers until 0 is entered. Compute and print out the sum of the odd
integers.
'''
sum =  0
while True:
    val = int(input("Enter integer: "))
    if val == 0: break
    if val % 2 != 0: sum += val

print("Sum of odd integers entered:", sum)
