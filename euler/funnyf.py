from decimal import Decimal as Dec, DivisionByZero
import functools

cur = []
for num in range(10,100,1):
    for den in range(num+1,100,1):
        if num%10 == 0 and den%10 == 0:
            continue
        # if den%num == 0:
        try:
            comdg = [c for c in str(num) if c in str(den)][0]
            fr = int(str(num).strip(comdg)),int(str(den).strip(comdg))
            if Dec(num)/Dec(den) == Dec(fr[0])/Dec(fr[1]):
                cur.append((num,den))
        except (IndexError, DivisionByZero, ValueError):
            pass
prod = functools.reduce(lambda x, y: x*y[0], cur, 1), \
    functools.reduce(lambda x, y: x*y[1], cur, 1)
# reduce this to primes to factor
print(prod)
