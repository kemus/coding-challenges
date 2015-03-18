from math import ceil

def divisors(n):
    d= [1]
    for i in range(2,int(ceil(n**.5))):
        if n%i == 0:
            d.append(i)
            d.append(n/i)
    return d

abundant = [x for x in range(1,20162) if sum(divisors(x)) > x]

def abundantSum(i):
    for x in abundant:
        if i-x in abundant:
            return True
        if x>i:
            return False
    return False

a=[]
for i in range(20162):
    if not abundantSum(i):
        print i
        a.append(i)
print sum(a)
