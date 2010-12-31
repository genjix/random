import primality, sys
from itertools import *
from functools import *

N = 100
primes = primality.primes(N)
nums = [False,]*N
nums[1] = 1,
for p in primes:
    if p > N:
        break

    basket = [False,]*N
    n = 1
    while p**n < N:
        for c in filter(lambda x: x, nums):
            getvalue = lambda parts : reduce(lambda acc, part: acc * part, parts, 1)
            v = tuple(chain(c, (p,)*n))
            val = getvalue(v)
            if val >= N:
                break
            basket[val] = v
        n += 1

    for i, n in filter(lambda x: x[1], enumerate(basket)):
        nums[i] = n

"""for n, p in enumerate(nums):
    if p:
        print n, reduce(lambda s, v: s + " %i"%(v,), p, "")"""

factorsasprimes = lambda x: set(chain(*map(lambda y: tuple(combinations(x, y)), range(1,len(x),1))))
factors = lambda x: tuple(map(lambda prtu: reduce(lambda a,b: a*b, prtu, 1), factorsasprimes(x)))
sumfactors = lambda x: sum(filter(lambda a: a != x, set(factors(nums[x]))))

numsums = tuple(map(sumfactors, range(1,N,1)))
# add indexs
#numsums = izip(range(1,len(numsums)+1,1), numsums)

abunums = tuple(map(lambda x: x[0], filter(lambda x: x[1] > x[0], zip(range(1,N,1), map(sumfactors, range(1,N,1))))))
print("abunums = (\\")
cr = 0
for n in abunums:
    sys.stdout.write(" %i,"%(n,))
    cr += 1
    if cr > 8:
        cr = 0
        print()
print(")")
