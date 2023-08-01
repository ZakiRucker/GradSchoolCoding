'''
8. Find and print out how many numbers are divisible by both 7 and 5 between two integers
low and high. Assume the values are already assigned to low and high, and low is less than
or equal to high.
'''
## We interpret 'between' to be exclusive
low = 10   ## dummy assignments
high = 100

cnt = 0
for i in range(low+1, high):
    if i % 7 == 0 and i % 5 == 0: cnt += 1
print(cnt)

cnt, i = 0, low+1
while i < high:
    if i % 7 == 0 and i % 5 == 0: cnt += 1
    i += 1
print(cnt)
