import decimal

def findrec(s):
    for i, b in enumerate(s):
        for j, c in zip(xrange(i+1,len(s),1), s[i+1:]):
            if c == b:
                eps = j - i
                while s[i:i+eps] == s[j:j+eps]:
                    j += eps
                    if j+eps > len(s):
                        return i, eps
    return 0,0

s = str(1/6.0)
print s, findrec(s)
decimal.getcontext().prec = 10000

z = []
bb = []
for i in xrange(1,1000,1):
    s = str(decimal.Decimal(1) / decimal.Decimal(i))
    z.append(findrec(s))
    bb.append(i)
gr = 0
for i in xrange(1000-1):
    if z[i][1] > z[gr][1]:
        gr = i
print i, z[gr], bb[gr]
print findrec(str(1/997.0))