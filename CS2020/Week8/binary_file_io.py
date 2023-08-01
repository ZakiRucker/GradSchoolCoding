#---------------------------------------------
# CS2020
#
# This program illustrates how save objects
# using the pickle module
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

from pickle import dump, load

productList = [
               ("11-1111", "screw driver", 6.95, 10),
               ("22-2222", "wrench",       9.95, 20),
               ("33-3333", "jig saw",     49.95, 15),
               ("44-4444", "hammer",      19.95, 40),
               ("55-5555", "chain saw",   99.95, 10)   
              ]
    
print()
print("Product:")
for item in productList:
    print(item)
    
## Now save the list to an object file
## Open the file using the "wb" mode for write binary
filename = input("Name of file to store a list of tuples: ")
file = open(filename, "wb")

dump(productList, file)

##Now open it and display the product information
## Open the file using the "rb" mode for read binary
filename = input("Name of file to read a list of tuples: ")
file = open(filename, "rb")

fileInputList = load(file)

print()
print("Product:")
for item in fileInputList:
    print(item)