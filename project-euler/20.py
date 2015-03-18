
def fact(x):
    if x == 1:
        return 1
    return x*fact(x-1)
print sum([int(x) for x in str(fact(100))])
