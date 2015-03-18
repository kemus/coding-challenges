from math import ceil

def divisors(n):
    d= [1]
    for i in range(2,int(ceil(n**.5))):
        if n%i == 0:
            d.append(i)
            d.append(n/i)
    return sorted(d)

print sum(divisors(sum(divisors(220))))
amicable = 0
for x in range(2,10000):
    y= sum(divisors(x))
    if y!=x and sum(divisors(y))==x:
        amicable+= x
print amicable
