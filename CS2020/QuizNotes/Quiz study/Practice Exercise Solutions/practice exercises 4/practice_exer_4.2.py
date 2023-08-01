'''
2. Create one long string by concatenating all strings entered by the user. Put one blank
space between the strings entered by the user. Use the while loop to repeatedly prompt
the user for input and stop the repetition when the user enters the string stop. The
stop keyword is case sensitive; all letters must be lowercase.
Do not include stop in the final result.
'''
result = ""
while True:
    val = input("Enter value: ")

    if val == "stop": break

    result = result + val + " "

result = result.strip()  ## remove the blank space at the end

print result
