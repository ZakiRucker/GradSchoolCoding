import csv

testList=[(10,20), (30,50)]

with open('test.txt', 'w') as myfile:
  wr = csv.writer(myfile) 
  wr.writerows(testList)