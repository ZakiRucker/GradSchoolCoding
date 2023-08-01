#---------------------------------------------
# CS2020
#
# Save three lines of text to a file
# named sample1.txt. We open the file in
# the write mode, write the desired data,
# and close the file
#
# It is a common practice to suffix the file
# name with txt for textfiles, but it is not
# a requirement. You can use any suffix you
# want.
#
# By default, the file is saved in the same
# directory where this program is stored.
#
# If the designated file already exists, then
# the previous contents will be erased. If the
# file does not exist, then a new one with
# the specified name is created.
#
# Python 3.0
#
# Author: Thomas Otani
#-------------------------------------------

#open the file in 'write' mode
myFile = open("sample1.txt", "w") #or "c:/python25/sample1.txt"
                                  # to specify specific folder + file

#write (save) three lines of text
myFile.write("Sample Line 1This is line 1.\n")
myFile.write("Sample Line 2 And here's line 2.\n")
myFile.write("Sample Line 3 Finally comes line 3.\n")

#for i in range(0,10):
#    myFile.write(str(i) + "  ")

#close the file
myFile.close()  #data get lost if you forget to close the file


