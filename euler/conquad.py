import primality, itertools

def countprimes(primes, a, b):
    score = 0
    for n in itertools.count():
        if n**2 + a*n + b not in primes:
            return score
        score += 1

primes = primality.primes(10000)
hiscore = 0, 0, 0
for a in range(-1000,1001):
    for b in range(-1000,1001):
        sc = countprimes(primes, a, b)
        if sc > hiscore[0]:
            hiscore = sc, a, b
print(hiscore)
