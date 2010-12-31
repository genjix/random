import math

def erat_core(ntab, n):
    i = 1
    while True:
        cx = ntab[i]
        if cx == False:
            i += 1
            continue
        if cx > n/2:
            break
        for j in xrange(2*cx, n, cx):
            try:
                #ntab.remove(j)
                ind = (j-1)/2
                ntab[ind] = False
            except ValueError:
                pass
        i += 1
    return ntab

def erat_sieve(n):
    ntab = range(1,n,2)
    ntab[0] = 2
    return erat_core(ntab, n)

def euler_sieve(n):
    # build a table of odd numbers.
    num_tab = list(range(1,n,2))
    # our table looks like 1,3,5,7,... we change the first
    # to the first prime, 2
    num_tab[0] = 2
    i = 1
    # biggest number in our table
    highestval = num_tab[-1]
    while True:
        # find first operator in the sieve
        cx = num_tab[i]
        # non working value so move to the next
        if cx == False:
            i += 1
            continue
        # first value to be sieved is always going to be
        # the current number * itself. all the next numbers in
        # that sieve will be larger.
        if cx**2 > n:
            break
        # strike off - our sieve
        tostrike = []
        for j in range(i,len(num_tab)):
            # find the second operator in the sieve
            cy = num_tab[j]
            # non-working value... skip over
            if cy == False:
                continue
            cut = cx*cy
            # outside the sieve's bounds
            if cut > highestval:
                break
            # add to our sieve
            tostrike.append(cut)
        # sieve the values from our number table
        for d in tostrike:
            ind = (d - 1)/2
            num_tab[int(ind)] = False
        # find the highest value in our number table that
        # hasn't been sieved
        hiind = -1
        while num_tab[hiind] == False:
            hiind -= 1
        highestval = num_tab[hiind]
        
        i += 1
    return num_tab

def primes(n):
    return [x for x in euler_sieve(n) if x != False]

if __name__ == "__main__":
    #print comp_sieve(30)
    print([x for x in euler_sieve(100) if x != False])
