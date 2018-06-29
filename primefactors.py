import random

n = 3999944000147

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

for a in range(2, n):
    # get greatest common divisor
    if gcd(a,n) == 1:
        r = False
        for period in range(1,10):
            if ((a**period) % n) == 1:
                r = period
                break


        fact = (a**(r/2))
        if period % 2 != 0 or (fact +1) % n == 0 or not r:
            continue
        p = gcd(fact-1, n)
        q = gcd(fact+1, n)
        print(p,q)
        break
