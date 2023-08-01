'''
10. Input 10 float numbers. Compute and print out their sum and average.
'''
sum = 0.0
for _ in range(10):
    sum += float(input("Enter float: "))
print(sum, sum / 10.0)

sum, i = 0.0, 0
while i < 10:
    sum += float(input("Enter float: "))
    i += 1
print(sum, sum / 10.0)
