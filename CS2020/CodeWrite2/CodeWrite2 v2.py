# Hello, Zaki
# CodeWrite2
# Zaki Rucker


import csv

testList=[(10,20), (30,50)]

with open('test.txt', 'w') as myfile: 
    wr = csv.writer(myfile)
    wr.writerows(testList)

"""row = map(int,row)
        
    print (row[0])
#get the numbers in a form I can use

x = row[0]
y = x-1
while y > 1:
    x *= y
    y -= 1
    

print x

def csvwrite(new_csv):
    outputfile =open('newNum.csv', "w")
    writer =csv.writer(outputfile)
    writer.writerrow(new_csv)

    outputfile.close()
    print (new_csv)"""
