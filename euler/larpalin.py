from math import floor

def ispalin(res):
    res = str(res)
    for n in xrange(len(res)/2):
        if res[n] != res[-n-1]:
            return False
    return True
		dslsd
if __name__ == "__main__":
    bigpalin = (0, 0, 0)
    for i in xrange(1000-1, 100-1, -1):
        for j in xrange(1000-1, 100-1, -1):
            res = i*j
            if ispalin(res) and res > bigpalin[2]:
                bigpalin = i, j, res
                #exit()
    print bigpalin
