import sys
def compcomp(number):
    return sum([int(c)**5 for c in str(number)])
if len(sys.argv) > 1:
    n = int(sys.argv[1])
    print(n, compcomp(n) - n)
else:
    sns = []
    for n in range(1,4000000,1):
        if compcomp(n) - n == 0:
            print(n)
            sns.append(n)
    print(sum(sns))
