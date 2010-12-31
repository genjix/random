from math import factorial as fact, floor
ncr = lambda r, n: fact(n)/(fact(r)*fact(n-r))
acc = 0
for n in range(2, 100+1):
    upn = floor(n/2)
    for r in range(1,upn+1):
        if ncr(r,n) > 10**6:
            print(ncr(r,n), upn)
            print(r,n, 2*(upn - r) + (1 - n%2) + 2*(n%2))
            acc += 2*(upn - r) + (1 - n%2) + 2*(n%2)
            break
print(acc)
