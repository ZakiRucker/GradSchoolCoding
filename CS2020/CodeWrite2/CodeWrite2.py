# Hello, Zaki
# CodeWrite2
# Zaki Rucker

import csv
testList=[(10,20), (30,50)]

with open('testNum.csv', 'w') as myfile:

wr = csv.writer(myfile)

wr.writerows(testList)


