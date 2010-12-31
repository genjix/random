f = open("keylog.txt")
codes = []
for l in f:
    codes.append(l[:-1])
print(codes)
db = {}
for entry in codes:
    lis = db.setdefault(entry[0], ([], []))
    lis[1].extend(entry[1:])
    lis = db.setdefault(entry[1], ([], []))
    lis[0].append(entry[0])
    lis[1].append(entry[2])
    lis = db.setdefault(entry[2], ([], []))
    lis[0].extend(entry[:2])
print(db)
for k, v in db.items():
    print(k)
    print("\t",v[0])
    print("\t",v[1])
# 73162890
