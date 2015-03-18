def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]

x= sorted(list(all_perms('0123456789')))
for i in range(len(x)):
    print i, x[i]
    if i == 1000000:
        break
