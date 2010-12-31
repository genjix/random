import random

grid = \
"""
------------------
--1000------------
-0000010001-------
-00100001000------
-10000000000------
-----0000000------
----1000000001----
--------0000------
---1100000000-----
--000000000001010-
-0100010000000000-
--00000000101010--
---1100100001100--
----------000-----
------------------
"""
grid = grid.split('\n')
grid = grid[1:-1]
ngrid = []
for line in grid:
    row = []
    for c in line:
        if c == '-':
            x = None
        elif c == '0':
            x = -1
        elif c == '1':
            x = 0
        else:
            x = 0
        row.append(x)
    ngrid.append(row)
grid = ngrid

####
start = (7, 8)

def renderGrid(pos, grid):
    render = ''
    for y, line in enumerate(grid):
        row = ''
        for x, cell in enumerate(line):
            if y == pos[0] and x == pos[1]:
                row += 'X'
            elif cell == None:
                row += '#'
            elif cell == -1:
                row += ' '
            else:
                row += str(cell) + ' '
        render += row + '\n'
    return render

print renderGrid(start, grid)

def monkey(pos, grid):
    while True:
        while True:
            choice = random.randint(0,3)
            if choice == 0:
                dir = (-1, 0)
            elif choice == 1:
                dir = (1, 0)
            elif choice == 2:
                dir = (0, -1)
            elif choice == 3:
                dir = (0, 1)
            npos = pos[0] + dir[0], pos[1] + dir[1]
            if grid[npos[0]][npos[1]] != None:
                pos = npos
                break
        #print renderGrid(pos, grid)
        #raw_input()
        if grid[pos[0]][pos[1]] >= 0:
            grid[pos[0]][pos[1]] += 1
            break

i = 0
while i < 1000000:
    monkey(start, grid)
    i += 1
print renderGrid(start, grid)
