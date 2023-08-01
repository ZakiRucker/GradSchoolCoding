#CS2020
#Zaki Rucker

import csv

"""def my_masterpiece(i):
    x = row()
    y = x-1
    while y > 1:
        x *= y
        y -= 1
    """
def csvopen():
    list = [] 
    with open('testNum.csv', 'r') as f:
        reader = csv.reader(f) 
        for row in reader: 
            row = map(int, row) 
            for i in row:
                list.append(my_masterpiece(i)) #running factorial and appending the results to the list

    csvwrite(list)

def csvwrite(new_csv):
    outputfile =open('newNum.csv', "w")
    writer =csv.writer(outputfile)
    writer.writerow(new_csv)

    outputfile.close()
    print (new_csv)


csvopen()

            
