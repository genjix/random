from itertools import count

def triples(constraint):
    fa, fb, fc = \
            lambda k, m, n: k*(m**2 - n**2), \
            lambda k, m, n: 2*k*m*n, \
            lambda k, m, n: k*(m**2 + n**2)
    ftrip = lambda k, m, n: (fa(k,m,n), fb(k,m,n), fc(k, m, n))
    triples = []
    for k in count(1):
        if not constraint(*ftrip(k, 2, 1)):
            break
        for n in count(1):
            if not constraint(*ftrip(k, n+1, n)):
                break
            for m in count(n+1):
                trips = ftrip(k,m,n)
                if not constraint(*trips):
                    break
                triples.append(trips)
    return triples
