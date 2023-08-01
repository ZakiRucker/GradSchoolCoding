'''
7. Find and print out how many numbers are divisible by 7 between two integers low and high.
Assume the values are already assigned to low and high, and low is less than or equal to
high.
'''
## We interpret 'between' to be exclusive
low = 10   ## dummy assignments
high = 100

cnt = 0
for i in range(low+1, high):
    if i % 7 == 0: cnt += 1
print(cnt)

cnt, i = 0, low+1
while i < high:
    if i % 7 == 0: cnt += 1
    i += 1
print(cnt)

## Another approach is to find the first number divisible by 7
## and then increment by 7 from that point
cnt = 0
low = 10
high = 100
for i in range(low+1, high):
    if i % 7 == 0: break

if i < high:
    for j in range(i, high, 7):
        cnt += 1
print(cnt)

cnt, i = 0, low+1
while i < high:
    if i % 7 == 0: break
    i += 1

if i < high:
    j = i
    while j < high:
        cnt += 1
        j += 7
print(cnt)
