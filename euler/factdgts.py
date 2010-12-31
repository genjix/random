from math import factorial
from itertools import count

fmap = [factorial(x) for x in range(10)]

def iscurious(n):
	rep = list(str(n))
	rep.sort()
	rep.reverse()
	acc = 0
	for dgt in rep:
		dgt = fmap[int(dgt)]
		if dgt > n:
			return False
		acc += dgt
		if acc > n:
			return False
	return acc == n
	#return sum([fmap[int(c)-1] for c in str(n)]) == n

acc = 0
for n in count(3):
	if iscurious(n):
		acc += n
		print(n, "is curious. Running total =", acc)
