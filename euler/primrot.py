import primality, itertools
primes = primality.primes(1000000)
acc = 0
for p in range(len(primes)):
    p = primes[p]
    prep = str(p)
    try:
        combos = 1
        for q in [prep[i:]+prep[:i] for i in range(1,len(prep))]:
            q = int(str(q))
            if q == p:
                continue
            combos += 1
            # mark q in primes if it exists
            primes.remove(q)
    except ValueError:
        continue
    acc += combos
    print(p,acc)
