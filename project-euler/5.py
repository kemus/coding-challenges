def primes_sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     # Mark factors non-prime
                a[n] = False


def factors(n):
    primes = primes_sieve(1+int(n**.5))
    for prime in primes:
        if n%prime ==0:
            return [prime]+factors(n/prime)
    return [n]

n=1
facts = {}
for j in range(2,20):
    new = {}
    for x in primes_sieve(21):
        new[x] = 0
    for f in factors(j):
        new[f]+=1
    for key,val in new.items():
        if key not in facts or facts[key]<val:
            facts[key]=val
out = 1
for k,v in facts.items():
    out *= k**v
print out
