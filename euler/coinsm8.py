def find_combos(target, coins):
    daddy = coins.pop()
    if daddy == 2 and len(coins) == 1:
        return target//2 + 1
    acc = 0
    for i in range(0,(target//daddy)+1,1):
        n = i*daddy
        rem = target - n
        if rem == 0:
            acc += 1
        else:
            acc += find_combos(rem, coins[:])
    return acc

coins = [1, 2, 5, 10, 20, 50, 100, 200]
target = 200
print(find_combos(target, coins))
