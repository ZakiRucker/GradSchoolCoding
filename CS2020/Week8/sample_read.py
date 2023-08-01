
#---------------------------------------------
# CS2020
#
# Read three lines of text from a file
# named sample1.txt. We open the file in
# the read mode, read the desired data,
# and close the file
#
# If the designated file does not exist or
# stored in nontext format, an error will
# result. By default, the designated file
# must reside in the same directory this
# program is stored
#
# Python 3.0
#
# Author: Thomas Otani
#-------------------------------------------

#open the file in 'read' mode
filename = input("enter filename:")
myFile = open(filename, "r")

#read three lines of text from the file and
#display them. Each line includes the newline
#control character. This results in having a
#blank line after each output line. You
#need to remove '\n' using the string method 
#rstrip as line.rstrip("\n")
#if you do not want this behavior
for cnt in range(3):
    line = myFile.readline()
   # line = line.rstrip("\n")
    print(line)
    
    
#The read method inputs the whole content of the file at once
#To try out this statement, comment out the above readline code
#print myFile.read()

#close the file
myFile.close()  #this is optional in case of read, but always safer
                #close when you're done with the file