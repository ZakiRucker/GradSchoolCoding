import csv
with open('testFlt.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        row = map(float, row)
        print row," ",len(row)," ",sum(row)