import itertools
sd = "123456789"
for s in itertools.permutations(sd, len(sd)):
    # convert s from a list to a string
    s = "".join(s)
    for i in range(1,len(sd)-1):
        firpar, c = s[:i], int(s[i-1:])
        for j in range(1,len(firpar)-1):
            a, b = int(s[:j]), int(s[j-1:])
            if a*b == c:
                print(a, b, c)

