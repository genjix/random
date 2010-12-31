"""
a^2 + b^2 = c^2

a + b + c = 1000
a + b + sqrt(a^2 + b^2) - 1000 = 0
a(a + b - 1000) + b(a + b - 1000) - 1000(a + b - 1000) = a^2 + b^2
a^2 + ab - 1000a + ab + b^2 - 1000b - 1000a - 1000b + 1000^2 =
a^2 + b^2 + 2ab - 2000a - 2000b + 1000^2 = a^2 + b^2

b = (1000^2/2 - 1000a) / (1000 - a)

a = 0 => b = 500
"""
from math import sqrt, ceil

for a in xrange(500):
    b = (1000**2/2 - 1000*a) / (1000 - a)
    b = round(b)
    c = sqrt(a**2 + b**2)
    c = round(c)
    s = a+b+c
    if s == 1000 and c**2 == a**2 + b**2:
        print a,b,c, a+b+c, ",", a*b*c