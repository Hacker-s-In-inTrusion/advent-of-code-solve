from aocd.models import Puzzle
from contextlib import suppress

p = Puzzle(2021, 9)
input_str = p.input_data
# input_str = """2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678"""

def check(point, map):
    x,y = point[0], point[1]
    my_val = map[x][y]
    up, down, right, left = (10,10,10,10)
    with suppress(IndexError): down = map[x + 1][y]
    with suppress(IndexError): right = map[x][y + 1]
    if x > 0 : up = map[x - 1][y]
    if y > 0 : left = map[x][y - 1]
    for i in (up, down, left, right):
        if i <= my_val: return -1
    return my_val

data = input_str.split("\n")
heightmap = []
for d in data:
    heightmap.append([int(x) for x in d])

score = 0
low_points = []
for x in range(len(heightmap)):
    for y in range(len(heightmap[x])):
        res = check((x,y), heightmap)
        if res != -1 : 
            low_points.append((x,y))
            score += (res + 1)

history = []
def basin_check(x,y,map):
    ret = []
    if map[x][y] == 8:
        return ret
    
    up = (x-1, y) if x > 0 else None
    down = (x + 1, y) if x < len(map) - 1 else None
    left = (x, y - 1) if y > 0 else None
    right = (x, y + 1) if y < len(map[x]) - 1 else None

    for i in [up,down,left,right]:
        if i == None:
            continue
        if map[i[0]][i[1]] == map[x][y] + 1:
            ret.append(i)
    return ret


def dfs_traverse_map(x,y,map):
    history.append((x,y))
    basin_points = basin_check(x,y,map)

    for _x, _y in basin_points:
        if (_x,_y) not in history:
            dfs_traverse_map(_x,_y,map)
    return

basin_size = []
for x,y in low_points:
    history = []
    dfs_traverse_map(x,y,heightmap)
    basin_size.append(len(history))

basin_size = sorted(basin_size)
print(basin_size[-1] * basin_size[-2] * basin_size[-3])