import primality, itertools
def ispand(n):
    nums = list(range(1,int(max(str(n)))+1))
    while len(nums) > 0:
        try:
            [nums.remove(int(x)) for x in str(n)]
        except ValueError:
            return False
    print(n)
    return True



primes = primality.primes(10000000)
[ispand(primes[n]) for n in itertools.count(0)]
