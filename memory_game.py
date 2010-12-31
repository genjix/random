import random, string, os, time

def rl():
    return string.uppercase[random.randint(0,len(string.uppercase)-1)]
def hamdist(s1, s2):
    assert len(s1) == len(s2)
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))
def test():
    rs = rl() + rl() + rl() + rl() + rl() + rl() + rl() + rl()
    print rs
    time.sleep(6)
    os.system("clear")
    ans = raw_input("8:")
    while len(ans) != 8:
	ans = raw_input("8:")
    errors = hamdist(ans, rs)
    print "Errors:", errors
    return errors

err = 0
for i in xrange(15):
    err += test()

print
print "Total:", err
