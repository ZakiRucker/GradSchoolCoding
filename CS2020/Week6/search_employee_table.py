#---------------------------------------------
# CS2020
#
# Search Employee Table.
#
# This sample program illustrates how the nested
# list is used to represent tabular data. We will
# search for employees whose salary fall between
# the given low and high values. We display only the
# name of the matching employees
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

employees = [["Ape", 20, 164, 10000.00],
             ["Bee", 42, 145, 50000.00],
             ["Cat", 35, 170, 50000.00],
             ["Dog", 23, 184, 43000.00],
             ["Eel", 28, 200, 55000.00],
             ["Fox", 69, 192, 67500.00],
             ["Gnu", 23, 156, 30000.00],
             ["Hen", 66, 180, 33000.00],
             ["Man", 34, 163, 90000.00],
             ["Pig", 55, 174, 75000.00],
             ["Tic", 23, 166, 34000.00],
             ["Yak", 33, 188, 23600.00]]

while True:
    low, high = eval(input("\nEnter low, high salaries (None,None to stop): "))
    
    if low == None and high == None: break
    
    result = []
    
    for emp in employees:
        if low <= emp[3] <= high:
            result += [emp[0]]  #or result.append(emp[0])
            
    print("")
    print(result)
    
print("Bye")