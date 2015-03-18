def primes_sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     # Mark factors non-prime
                a[n] = False


p=list(primes_sieve(2000000))
pp=list(primes_sieve(2000))
maxx = 0
for b in pp:
    for a in range(-1*b,1):
        amod = a%2
        if b!=2 and amod == 0:
            continue
        if b==2 and amod ==1:
            continue
        if a+b+1 not in p:
            continue
        n = 0
        while((n**2+a*n+b) in p):
            n+=1
        if n > maxx:
            maxx = n
            print a,b,maxx
