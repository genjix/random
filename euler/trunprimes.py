import primality
class NotTruncatable(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
            
primes = primality.primes(1000000)
acc, count = 0, 0
for prime in primes:
    if prime < 10:
        continue
    re = str(prime)
    try:
        for l in range(len(re)-1,0,-1):
            if int(re[-l:]) not in primes or int(re[:l]) not in primes:
                raise NotTruncatable(prime)
        acc += prime
        count += 1
        print(prime)
    except NotTruncatable as e:
        #print(e.value, "is non-truncatable")
        pass
print("sum =", acc, ", count =", count)
