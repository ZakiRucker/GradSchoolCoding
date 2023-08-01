#CS2020
#Zaki Rucker

import csv

def factorial(i):
    d = 1
    while (i > 0):
        d = d * i
        i = i - 1
    return d
    
def csvopen():
    list = [] #makes blank list
    with open('testNum.csv', 'r') as f:#reads "r" csv and assigns it to f
        reader = csv.reader(f) #takes f and turns it into reader
        for row in reader: #starts looping through the rows in the csv
            row = map(int, row) #takes the row and maps them to a list of integers
            #print row," ",len(row)," ",sum(row) #displays the lenth of all integers in the row and adds them together
            for i in row:
                list.append(factorial(i)) #running factorial and appending the results to the list
    csvwrite(list)

def csvwrite(new_csv):
    outputfile =open('newNum.csv', "w")
    writer =csv.writer(outputfile)
    writer.writerow(new_csv)

    outputfile.close()
    print (new_csv)


csvopen()

            
