'''
12. Using while, input integers until 0 is entered. Find and print out how many of them are even
integers.
'''
cnt =  0
while True:
    val = int(input("Enter integer: "))
    if val == 0: break
    if val % 2 == 0: cnt += 1

print("No of integers entered:", cnt)
