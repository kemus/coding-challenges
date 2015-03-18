mem = {0:0, 1:1}
def fib(x):
    if x not in mem:
        mem[x] = fib(x-1)+fib(x-2)
    return mem[x]


x = 0
out = 0
i = 0
while len(str(x)) < 1000:
    i+=1
    x= fib(i)

print i
