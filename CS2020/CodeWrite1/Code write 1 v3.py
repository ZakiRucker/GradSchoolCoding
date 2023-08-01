
##Hello, Zaki
##This is a code write lab.
##1) Start with the Helloworld.py program.<
##2) Use sample code from Prof Otani, using foreach, IF and function calls.<
##3) Do not use any other code from elsewhere (web).<
##4) Rewrite the factorial to input a number, check for -ve/+ve, 0, 1.
##5) use a function to calculate the factorial (do NOT use the recursive solution from the web).<
##6) now use the CSV code that I have supplied, use that to read a file of numbers, read it into an array and repeatedly calculate the factorial and print out.
##7) Show the tested and completed program with all steps.

import csv

with open('testnum.csv', 'r') as f: 
    reader = csv.reader(f)
    for row in reader:
        row = map(int,row)
        
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
    print (new_csv)
