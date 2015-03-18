isPalindrome = lambda n: str(n)==str(n)[::-1]

maxx = 0
for i in range(999,900,-1):
    for j in range(999,900,-1):
        x= i*j
        if isPalindrome(x) and x>maxx:
            maxx = x
            print maxx
