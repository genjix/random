from math import sqrt, floor
# first triangle number to have > 500 divisors

def count_div(n):
    nd = 0
    for x in xrange(1,int(1+floor(sqrt(n))),1):
        if n%x == 0:
            nd += 1
    return nd*2

sum = lambda n: n*(n+1)/2

if __name__ == "__main__":
    n = 360 # (500/2)**2 = 62500, n ~= 360
    sn = sum(n)
    while True:
        if sn%2 == 0 and sn%3 == 0 and count_div(sn) > 500:
            print sn
            break
        n += 1
        sn += n
