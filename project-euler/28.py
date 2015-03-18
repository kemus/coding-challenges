x = 1
mul = 2
diagsum = 1
for layer in range(500):
    for i in range(4):
        x+=mul
        diagsum+=x
    mul+=2

print diagsum
