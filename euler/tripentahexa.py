from math import sqrt
from itertools import count
# Tn = n(n+1)/2
# n = sqrt(2Tn + 1/4) - 1/2
Tn = lambda n: n*(n+1)/2
invTn = lambda Tn: sqrt(2*Tn + 1/4) - 1/2

# Pn = n(3n-1)/2
# n = sqrt(2Pn/3 + 1/36) + 1/6
Pn = lambda n: n*(3*n-1)/2
invPn = lambda Pn: sqrt(2*Pn/3 + 1/36) + 1/6

# Hn = n(2n-1)
# n = sqrt(Hn/2 + 1/16) + 1/4
Hn = lambda n: n*(2*n-1)
invHn = lambda Hn: sqrt(Hn/2 + 1/16) + 1/4

# Hn > Pn > Tn
isint = lambda x: abs(x - round(x)) < 0.1

for n in count(286):
    t = Tn(n)
    ip = invPn(t)
    if isint(ip) and Pn(round(ip)) == t:
        ih = invHn(t)
        if isint(ih) and Hn(round(ih)) == t:
            print(t)
            break
