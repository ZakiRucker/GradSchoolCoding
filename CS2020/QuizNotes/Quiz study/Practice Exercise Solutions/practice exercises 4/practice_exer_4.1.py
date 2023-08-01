'''
1. Create a list of strings by inputting strings from the user. Use the while loop to
repeatedly prompt the user for input and stop the repetition when the user enters the
string stop. The stop keyword is case sensitive; all letters must be lowercase.
'''
strs = []
while True:
    val = input("Enter value: ")

    if val == "stop": break

    strs.append(val)
    print strs
    ## or ##
    # strs += [val]

