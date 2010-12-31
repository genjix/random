from itertools import count
def samem(x):
    sx = str(x)
    for mult in range(1,7):
        sy = str(mult*x)
        for c in sy:
            if c not in sx:
                return False
    return True                
for i in count(1):
    if samem(i):
        print(i)
        break
