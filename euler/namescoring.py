f = open("names.txt")
names = f.readline().replace("\"", "").split(",")
names.sort()
letval = lambda c: ord(c) - (ord("A") - 1)
score = lambda i: i * reduce(lambda v, c: letval(c) + v, names[i - 1], 0)
print sum([score(i) for i in xrange(len(names)+1)])

