"""
1) Read each line of this file and create a list of different names
    (column 1 of the CSV).
2) Read each line of the file and then create a dictionary with name as key
    and the frequency count of the word Python.
3) Read each line of the file and then create a dictionary with name as key
    and the frequency count of the word Java.

Programming style:
Imports
functions (most dependent comes first and less dependent go below)
Main:

Initialize your lists and dictionaries as empty.
Read the data using the CSV library functions
Create the various asked lists and dictionaries (1 list of all people and 2 dictionaries, one for Python and one for Java)
"""
import csv

with open('quotes.csv') as csvfile:
 """   qreader = csv.reader 
    for row in qreader:
         print row
"""
 print csvfile
 
