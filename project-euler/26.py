from decimal import *
import re
getcontext().prec=50

def recurr(s):
    remainderList = []
    count = 0
    remainder = 1
    while remainder != 0:
        remainder %= s
        if remainder in remainderList:
            return count - remainderList.index(remainder)
        remainderList.append(remainder)
        remainder *=10
        count+=1
    return 0
m = 0
for i in range(1,1000):
    if recurr(i)>m:
        print i, recurr(i)
        m=recurr(i)
