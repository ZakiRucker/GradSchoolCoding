import csv
with open('testTxt.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print row," ",len(row)