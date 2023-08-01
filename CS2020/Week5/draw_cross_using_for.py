#---------------------------------------------
# CS2900
#
# This program draws a cross. Notice how the
# formatting string is constructed.
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

#This draws a reverse diagonal \
for i in range(1, 11):
   format = "%"+ str(i) + "s"
   print(format % "*")

#This draws a diagonal /
for i in range(1, 11):
   format = "%"+ str(11-i) + "s"
   print(format % "*")
  
#And this draws both the forward and reverse diagonals
#to form a cross. We draw a cross by drawing a V and
#the reverse V, 
for i in range(1, 6):
   format = "%"+ str(i) + "s" + "%"+ str(11-2*i) + "s"
   print(format % ("*", "*"))
   
for i in range(1, 6):  #you can use 2 for the lower bound
   format = "%"+ str(6-i) + "s" + "%"+ str(2*i-1) + "s"
   print(format % ("*", "*"))
   
#Exercise: Define a function drawCross that accepts one
#          parameter N, where N determines the size of
#          of the cross. N is 11 in the previous example.
#          What would be the smallest valid N?
#
   
   