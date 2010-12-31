import functools, itertools
def stopat(s):
    if len(s) == 0:
        yield "0"
    elif s[-1] in ("x", "="):
        yield s.pop()
    else:
        while len(s) > 0:
            if s[-1] in ("x", "="):
                break
            c = s.pop()
            yield c

def tryconv(s):
    if s in ("x", "="):
        return s
    return int(s)

def computestr(s):
    s = list(s)
    s.reverse()
    expr = \
            tryconv(functools.reduce(lambda x, y: x+y, stopat(s), "")),\
            tryconv(functools.reduce(lambda x, y: x+y, stopat(s), "")),\
            tryconv(functools.reduce(lambda x, y: x+y, stopat(s), "")),\
            tryconv(functools.reduce(lambda x, y: x+y, stopat(s), "")),\
            tryconv(functools.reduce(lambda x, y: x+y, stopat(s), ""))

    OP_A = 0
    OP_MULT = 1
    OP_B = 2
    OP_EQ = 3
    OP_RES = 4

    reg, state = 0, OP_A
    for evl in expr:
        if evl == 0:
            return False
            break
        if state == OP_A:
            if evl in ("x", "="):
                return False
                break
            state = OP_MULT
            reg = evl
        elif state == OP_MULT:
            if evl != "x":
                return False
                break
            state = OP_B
        elif state == OP_B:
            if evl in ("x", "="):
                return False
                break
            reg = reg * evl
            state = OP_EQ
        elif state == OP_EQ:
            if evl != "=":
                return False
                break
            state = OP_RES
        elif state == OP_RES:
            if evl in ("x", "="):
                return False
                break
            reg = (reg == evl)
    return reg

print(computestr("12x12=1484"))
allchars = "123456789x="
for s in itertools.permutations(allchars, len(allchars)):
    if computestr(s):
        print(s)
