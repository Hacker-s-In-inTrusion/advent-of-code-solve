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

def basin_check(x,y,map):
    my_val = map[x][y]
    if (my_val == 9) or (my_val == 8):
        return []
    ret = []
    with suppress(IndexError):
        if map[x + 1][y] == my_val + 1:
            ret.append((x+1, y))
    with suppress(IndexError):
        if map[x][y + 1] == my_val + 1:
            ret.append((x, y + 1))
    if x > 0 :
        if map[x - 1][y] == my_val + 1:
            ret.append((x - 1, y))
    if y > 0 :
        if map[x][y - 1] == my_val + 1:
            ret.append((x, y - 1))
    return ret


def traverse_map(x,y,map):
    basin = [(x,y)]
    p = basin_check(x,y,map)
    if len(p) == 0:
        return 1
    while True:
        x,y = p.pop()
        basin.append((x,y))
        quarantine = basin_check(x,y,map)
        for _q in quarantine:
            if _q not in basin:
                p.append(_q)
        if len(p) == 0:
            break
    
    return len(basin)
basin_size = []
for x,y in low_points:
    basin_size.append(traverse_map(x,y,heightmap))

basin_size = sorted(basin_size)
print(basin_size)
print(basin_size[-1] * basin_size[-2] * basin_size[-3])