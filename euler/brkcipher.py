import itertools
with open("cipher1.txt") as f:
    read_data = f.read()
read_data = [int(z) for z in read_data.split(",")]
words = "the", "be", "to"
def rcom(): return range(ord("a"), ord("z")+1)
for a in rcom():
    for b in rcom():
        for c in rcom():
            translated = "".join(list(map(lambda x, y: chr(int(x)^int(y)), read_data, itertools.cycle((a, b, c)))))
            if "John" in translated:
                print(translated)
                print(chr(a),chr(b),chr(c))
                print(sum(map(lambda x, y: int(x)^int(y), read_data, itertools.cycle((a, b, c)))))
                raise Exception()
