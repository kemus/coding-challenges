d = {(20,20):1}
def path(x,y):
    global d
    if x>20 or y>20:
        return 0
    if (x,y) in d:
        return d[(x,y)]

    d[(x,y)] = path(x+1,y) + path(x,y+1)
    return d[(x,y)]

print path(0,0)
