import pythagtrip
trips = pythagtrip.triples(lambda a,b,c: a+b+c <= 1001)
perim = {}
for t in trips:
    p = sum(t)
    if p in perim:
        swa = t[1], t[0], t[2]
        if not swa in perim[p] and not t in perim[p]:
            perim[p].append(t)
    else:
        perim[p] = [t]
larg = 0
for p, tr in perim.items():
    print(p, len(tr))
    if len(tr) > larg:
        larg = p
        print(p,tr)
print(perim[larg], larg)
