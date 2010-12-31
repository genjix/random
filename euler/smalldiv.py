def evdiv(n):
    for i in xrange(11,21,1):
        if n%i != 0:
            return False
    return True

if __name__ == "__main__":
    divs = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    n = 1
    for i in divs:
        n *= i
    print n
    for n in xrange(2520, n, 2):
        if evdiv(n):
            print n
            exit()
