import itertools
for pan in itertools.permutations("123456789"):
    pan = "".join(pan)
    for i in range(1,len(pan)//2+1,1):
        concat = pan[:i]
        mult = int(concat)
        z = 1
        while len(concat) < len(pan):
            z += 1
            concat += str(z*mult)
        if concat == pan:
            print(pan, mult, z)
