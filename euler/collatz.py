def chain(n):
    c = 1
    while n != 1:
        if n%2 == 0:
            n >>= 1
        else:
            n *= 3
            n += 1
        c += 1
    return c
lonch = 0
lonn = 0
for n in xrange(1000000,1,-1):
    chlen = chain(n)
    if lonch < chlen:
        lonn = n
        lonch = chlen
    if n%10 == 0:
        print n, lonn
print lonch, lonn
