d = {1:1, 2:2}

def collatz(y):
    global d
    if y in d:
        return d[y]
    d[y]=1+collatz([y/2,3*y+1][y%2])
    return d[y]

maximum = 0
maxx = 0
for x in range(1, 1000000):
    c = collatz(x)
    if c>maximum:
        maximum=c
        maxx=x
print maxx
