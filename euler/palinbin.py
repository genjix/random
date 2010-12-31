decbin = lambda d: (d < 2 and str(d%2)) or decbin(d//2) + str(d%2)
palindrome = lambda s: s == s[::-1]
bothpal = lambda n: palindrome(str(n)) and palindrome(decbin(n))
acc = 0
for i in range(1, 1000000, 2):
    if bothpal(i):
        acc += i
        print(i)
print(acc)
