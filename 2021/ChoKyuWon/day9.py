from aocd.models import Puzzle
from contextlib import suppress

p = Puzzle(2021, 9)
input_str = p.input_data
input_str = """2199943210
3987894921
9856789892
8767896789
9899965678"""

def check(point, map):
    x,y = point[0], point[1]
    my_val = map[x][y]
    up = 10
    down = 10
    right = 10
    left = 10
    with suppress(IndexError): down = map[x + 1][y]
    with suppress(IndexError): right = map[x][y + 1]
    if x > 0 : up = map[x - 1][y]
    if y > 0 : left = map[x][y - 1]
    m = min(my_val, up, down, right, left)
    # print("({}, {}):".format(x,y), my_val, up, down, right, left, "min:{}".format(m))
    if  m == my_val:
        return my_val
    else:
        return -1

data = input_str.split("\n")
heightmap = []
for d in data:
    heightmap.append([int(x) for x in d])

score = 0
for x in range(len(heightmap)):
    for y in range(len(heightmap[x])):
        res = check((x,y), heightmap)
        if res != -1 : 
            print(x,y)
            score += (res + 1)
print(score)