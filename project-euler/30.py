s=0
for i in range(2,9**5*6):
    if sum([int(j)**5 for j in str(i)]) == i:
        print i
        s+=i
print s
