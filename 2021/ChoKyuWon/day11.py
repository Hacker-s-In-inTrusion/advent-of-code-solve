from aocd.models import Puzzle
from contextlib import suppress

p = Puzzle(2021, 11)
input_str = p.input_data
# input_str="""5483143223
# 2745854711
# 5264556173
# 6141336146
# 6357385478
# 4167524645
# 2176841721
# 6882881134
# 4846848554
# 5283751526"""

data = input_str.split("\n")

octopus_map = [[] for i in range(len(data))]
for line in data:
    for i,ch in enumerate(line):
        octopus_map[i].append(int(ch))


def propagate(x,y,map):
    map[x][y] = None
    neg_x = None if x == 0 else x -1
    pos_x = None if x >= len(map) - 1 else x + 1
    neg_y = None if y == 0 else y -1
    pos_y = None if y >= len(map[0]) - 1 else y + 1
    x_array = [neg_x, x, pos_x]
    y_array = [neg_y, y, pos_y]
    for _x in x_array:
        for _y in y_array:
            with suppress(TypeError):
                    map[_x][_y] += 1

def stepping(octopus_map):
    flash_count = 0
    for x in range(len(octopus_map)):
        for y in range(len(octopus_map[0])):
            octopus_map[x][y] += 1
    while True:
        tmp = 0
        for x in range(len(octopus_map)):
            for y in range(len(octopus_map[0])):
                if octopus_map[x][y] == None:
                    continue
                if octopus_map[x][y] > 9:
                    propagate(x,y,octopus_map)
                    tmp += 1
        if tmp == 0:
            break
    for x in range(len(octopus_map)):
        for y in range(len(octopus_map[0])):
            if octopus_map[x][y] == None :
                flash_count += 1
                octopus_map[x][y] = 0
    return flash_count

# Part 1
step = 100
flash = 0
for i in range(step):
    flash += stepping(octopus_map)
print(flash)

# Part 2
octopus_map = [[] for i in range(len(data))]
for line in data:
    for i,ch in enumerate(line):
        octopus_map[i].append(int(ch))
count = 0
while True:
    tmp = stepping(octopus_map)
    count += 1
    if(tmp == len(octopus_map)**2):
        break
print(count)