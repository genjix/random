import primality
from itertools import *

N = 1000
primes = primality.primes(N)
nums = [False,]*N
nums[1] = 1,
for p in primes:
    if p > N:
        break

    basket = [False,]*N
    n = 1
    while p**n < N:
        for c in ifilter(lambda x: x, nums):
            getvalue = lambda parts : reduce(lambda acc, part: acc * part, parts, 1)
            v = tuple(chain(c, (p,)*n))
            val = getvalue(v)
            if val >= N:
                break
            basket[val] = v
        n += 1

    for i, n in ifilter(lambda x: x[1], enumerate(basket)):
        nums[i] = n

"""for n, p in enumerate(nums):
    if p:
        print n, reduce(lambda s, v: s + " %i"%(v,), p, "")"""

factorsasprimes = lambda x: set(chain(*imap(lambda y: tuple(combinations(x, y)), range(1,len(x),1))))
factors = lambda x: tuple(imap(lambda prtu: reduce(lambda a,b: a*b, prtu, 1), factorsasprimes(x)))
sumfactors = lambda x: sum(ifilter(lambda a: a != x, set(factors(nums[x]))))

numsums = tuple(imap(sumfactors, range(1,N,1)))
# add indexs
#numsums = izip(range(1,len(numsums)+1,1), numsums)

acc = 0
for n, i in izip(xrange(2,N-1,1),numsums[1:]):
    try:
        if i != n and numsums[i-1] == n:
            print n, i
            acc += n
    except IndexError:
        continue
print acc

