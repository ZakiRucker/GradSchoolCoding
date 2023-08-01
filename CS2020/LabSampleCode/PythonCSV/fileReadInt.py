import csv
with open('testNum.csv', 'r') as ZR:
    reader = csv.reader(ZR)
    for row in reader:
        row = map(int, row)
        print row," ",len(row)," ",sum(row)
