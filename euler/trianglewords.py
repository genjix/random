import itertools
f = open("words.txt")
words = f.read().replace("\"", "").lower().split(",")
# the longest word in the list is 14 chars
# 364 is the word value of "z"*14
letval = lambda c: ord(c) - ord("a") + 1
wordval = lambda w: letval(w[0]) + (len(w) > 1 and wordval(w[1:]) or 0)
trin = lambda n: n*(n+1)//2
firtris = []
for n in itertools.count(1):
    n = trin(n)
    if n > 364:
        break
    firtris.append(n)
triwords = [w for w in words if wordval(w) in firtris]
print(len(triwords))
