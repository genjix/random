from itertools import count
def finddig(n):
    n -= 1
    # keep removing smaller spaces until we arrive
    # at our digit space
    # space for 1389 would be 1000 with ex = 3
    # subspaces are 100, 10 and 1 within that
    space = 0
    for ex in count(1):
        space_expans = ex*(10**ex - 10**(ex - 1))
        if space_expans + space > n:
            n -= space
            break
        space += space_expans
    # which digit do we want in our number- starts from 0 upwards
    dsel = n%ex
    # add in an offset for subspaces underneath our space with padded 0's
    # [0001, 0002, ... , 0123, 0124, ... , 0988, 0999,] 1000
    n += ex * 10**(ex-1) 
    # now divide by the number of digits for each number
    # like the string for 0001 to 1000 would be 1000 * 4
    n //= ex
    # select the number from the digit
    return int(str(n)[dsel])

if __name__ == "__main__":
    import functools
    def dounittest(s):
        import random
        r = random.randint(1,10000)
        d = str(finddig(r))
        test = d == s[r]
        print(d, s[r], test)
    s = ""
    for n in range(10000):
        s += str(n)
    dounittest(s)
    dounittest(s)
    dounittest(s)
    dounittest(s)
    for i in range(1,30):
        d = str(finddig(i))
        print(d, s[i], d == s[i])
    print(finddig(12))
    ans = functools.reduce(lambda x, y: x*y, [finddig(10**p) for p in range(6+1)])
    print(ans)
