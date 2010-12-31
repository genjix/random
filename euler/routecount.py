from math import floor

def triangle_num(num, depth):
    if depth < 1:
        return num
    newnums = [1]
    for i, n in enumerate(num[:-1]):
        newnums.append(n + num[i+1])
    newnums.append(1)
    return triangle_num(newnums, depth-1)

tri = triangle_num([1], 2*20)
print tri, tri[int(floor(len(tri)/2))]