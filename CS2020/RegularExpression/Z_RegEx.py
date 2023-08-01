## Hello, Zaki
## 2.7

import csv
import re

SSN = []
Valid_CS_Course = []
Python_dict = {}
Java_dict = {}

with open('RegExp.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter='|')
    for row in reader:
        if re.match(r"\d\d\d-\d\d-\d\d\d\d$", row[1]):
            SSN.append(row[0])
        if re.match(r"(386|389)-[0-9][0-9](1|4)$", row[2]):
            Valid_CS_Course.append(row[0])
        Python_dict[row[0]] = len(re.findall(r"[pP]ython\W", row[3]))
        Java_dict[row[0]] = len(re.findall(r'[jJ]ava\W', row[3]))

print SSN
print Valid_CS_Course
print Python_dict
print Java_dict


