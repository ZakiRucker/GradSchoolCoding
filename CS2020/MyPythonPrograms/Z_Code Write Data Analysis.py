# Hello, Zaki
# 2.7
# Data Analysis

import csv

names = []
python = {}
java = {}

with open('quotes.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
            names.append(row[0])
            python[row[0]] = 0
            java[row[0]] = 0
            for word in row[1].split():
                 if word.lower() == 'python':
                     python[row[0]] += 1
                 elif word.lower() == 'java':
                     java[row[0]] += 1

print(names)
print(python)
print(java)
