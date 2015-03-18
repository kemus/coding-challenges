from math import ceil
def tri(n):
    return sum(range(n+1))

def divisors(n):
    d= []
    for i in range(1,int(ceil(n**.5))):
        if n%i == 0:
            d.append(i)
            d.append(n/i)
    return sorted(d)

x=0
while True:
    x+=1
    t = tri(x)
    d = divisors(t)
    if len(d) > 500:
        print t
        break
