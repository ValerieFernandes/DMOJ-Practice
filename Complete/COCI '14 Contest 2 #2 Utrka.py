##participants = int(input())
##
##names = []
##
##for i in range(participants * 2 - 1):
##    names.append(input())
##  
##
##for i in range (participants):
##    if names.count(names[i]) % 2 == 1:
##        print(names[i])
##        break


##participants = int(input())
##
##names = []
##
##for i in range(participants):
##    names.append(input())
##
##for i in range(participants - 1):
##    names.clear(input())
##
##print(names[0])


##participants = int(input())
##
##names = []
##
##for i in range(participants * 2 - 1):
##
##    temp = input()
##    if temp in names:
##        names.remove(temp)
##
##    else:
##        names.append(temp)
##
##print(names[0])






##participants = int(input())
##
##names = []
##
##for i in range(participants * 2 - 1):
##    names.append(input())
##
##
##names.sort()
##def name(names):
##
##    for i in range (0, (len(names) - 1), 2):
##
##        if names[i] != names[(i + 1)]:
##            return(names[i])
##
##    return(names[-1])
##
##print(name(names))

    
from collections import Counter

import math

participants = int(input())

names = []

finish = []

for i in range(participants):
    names.append(input())
  

for i in range (participants, participants * 2 - 1):
    finish.append(input())
    

temp1 = Counter(names)

temp2 = Counter(finish)

difference = temp1 - temp2

print(temp1)












































