import math

def isprime(cx, primes):
    for p in primes:
        if cx%p == 0:
            return False
    return True

def badprimetest(n):
    ntab = range(2,n,1)
    for x in ntab:
        print ntab
        for j in xrange(x+x, n, x):
            try:
                ntab.remove(j)
            except ValueError:
                pass
    for x in ntab:
        if n%x == 0:
            return True
    return False

if __name__ == "__main__":
    #print badprimetest(6857)
    n = 600851475143
    primes = []
    pdiv = []
    cx = 2
    while True:
        if isprime(cx, primes):
            primes.append(cx)
            if n%cx == 0:
                pdiv.append(cx)
                while n%cx == 0:
                    print n
                    n /= cx
            if cx > n/cx:
                break
        cx += 1
    print pdiv, n