
#---------------------------------------------
# CS2020
#
# This illustrates the reading of record
# data from a textfile. The file 'common names.txt'
# contains a list of 1000 common surnames. Each
# line is in the following format:
#
#        name     count    percentage
#        SMITH	  2501922  1.006
#
# It shows that there are 2,501,922 Smiths and
# that's 1.006 percent of the population
#
# The list will contain 1000 records, with each
# record also represented as a list:
# [ ['Smith', 2501922, 1.006],
#   ['Johnson',	2014470, 0.81],
#   ['Williams,	1738413, 0.699],
#     ...
#   ['Vang',29844, 0.012]]
#
# Python 3.0
#
# Author: Thomas Otani
#
#-------------------------------------------

NAME    = 0
COUNT   = 1
PERCENT = 2

namefile = open("common names.txt", "r")

namelist = []

for line in namefile:
    list = line.split() #split a single string into pieces
    
    list[NAME]    = list[NAME].capitalize() #SMITH   --> Smith
    list[COUNT]   = int(list[COUNT])        #"98776" --> 98776
    list[PERCENT] = float(list[PERCENT])    #"0.768" --> 0.768
    
    namelist.append(list) #add this record to the list
    
limit = len(namelist)
    
print("%5d: %s" % (1, namelist[0][NAME]))
print("%5d: %s" % (limit, namelist[limit-1][NAME]))

while True:
    searchName = input("Name to Search (Enter nothing to stop): ")
    
    if searchName == "": break
    
    searchName = searchName.capitalize()
            
    idx = 1;
    for item in namelist:
        
        if item[NAME] == searchName:
            print("Found. %s is Rank %d. %d people share this name" % \
                   (searchName, idx, item[COUNT]))
            break
        
        idx += 1
    
    else:
        print("Not Found. %s is not in the top 1000 list" % searchName)

namefile.close()



    
    