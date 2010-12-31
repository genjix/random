vals = []
for a in xrange(2,101,1):
    for b in xrange(2,101,1):
        x = a**b
        if x not in vals:
            vals.append(x)
print len(vals)
