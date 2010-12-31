import code
sfr = ""
for i in range(1,200,1):
    sfr += str(i)
for i, d in enumerate(sfr):
    print(i+1, d)
fd_hi = lambda n: 1 + (n - 10)//20
fd = lambda n: fd_hi(n)*((n+1)%2) + ((n - 10)//2 - (fd_hi(n-1) - 1)*10)*(n%2)
for i in range(1,200,1):
    print(i, sfr[i-1], fd(i))
