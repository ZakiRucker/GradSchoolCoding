'''
10. Given a string S, print out one character from both ends per line.
When S is "HELLO" the output will be
H  o
e  l
l  l
l  e
o  H
'''
S = "Hello" ## test assignment

## Direct ##

'''Direct approach is not relevant for this task'''

## For Index ##
for i in range(len(S)):
    print(S[i], S[-(i+1)])

## While Index ##
i = 0
while i < len(S):
    print(S[i], S[-(i + 1)])
    i += 1


