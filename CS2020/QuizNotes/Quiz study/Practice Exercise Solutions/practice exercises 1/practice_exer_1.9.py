'''
9. Compute and print out the sum of integers between num1 and num2. You do not know
which one is larger.
'''
## We interpret 'between' to be exclusive
num1 = 150   ## dummy assignments
num2 = 100

low, high = (num1, num2) if num1 < num2 else (num2, num1)

sum = 0
for i in range(low+1, high):
    sum += i
print(sum)

sum = 0
i = low+1
while i < high:
    sum += i
    i += 1
print(sum)
