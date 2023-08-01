'''
1. Create a list of integers by inputting values from the user. Assume the user will
enter valid values only. Use the while loop to repeatedly prompt the user for input
and stop the repetition when the user enters 0.
'''
xs = []
while True:
    val = int(input("Enter value: "))

    if val == 0: break

    xs.append(val)
    print xs
    ## or ##
    # xs += [val]

