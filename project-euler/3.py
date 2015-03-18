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
print factors(600851475143)
