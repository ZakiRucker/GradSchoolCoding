'''
14. Using while, input integers until 0 is entered. Find and print out the maximum and the
minimum of the integers read.
'''
val = int(input("Enter integer: "))
if val == 0:
    print(("No numbers entered"))

else:
    mn = val
    mx = val

    while True:
        val = int(input("Enter integer: "))
        if val == 0: break

        if val < mn: mn = val
        elif val > mx : mx = val

    print("min:", mn, " max:", mx)
