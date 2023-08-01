'''
11. Using while, input float numbers until 0 is entered. Compute and print out their sum and
average. Do not include the terminator value 0 in the computation.
'''
sum, cnt = 0.0, 0
while True:
    val = float(input("Enter float: "))
    if val == 0: break
    cnt += 1
    sum += val

print(sum, sum / cnt)
