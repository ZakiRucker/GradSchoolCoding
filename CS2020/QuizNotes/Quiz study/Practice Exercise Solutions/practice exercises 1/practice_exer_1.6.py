'''
6. Compute and print out the sum of integers between low and high. Assume the values are
already assigned to low and high, and low is less than or equal to high.
'''
## We interpret 'between' to be exclusive, so we are computing
## low+1 ... high-1. If low is equal to high or high-1, then sum is 0

low = 10   ## dummy assignments
high = 100

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
