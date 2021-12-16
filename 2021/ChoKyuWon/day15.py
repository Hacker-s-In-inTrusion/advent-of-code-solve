from aocd.models import Puzzle
p = Puzzle(2021, 15)
input_str = p.input_data
# input_str="""1163751742
# 1381373672
# 2136511328
# 3694931569
# 7463417111
# 1319128137
# 1359912421
# 3125421639
# 1293138521
# 2311944581"""

data = input_str.split("\n")
cave = [[0]*len(data[0]) for _ in range(len(data))]
min_val = [[1<<32]*len(data[0]) for _ in range(len(data))]

for y in range(len(data)):
    for x in range(len(data[0])):
        cave[y][x] = int(data[y][x])

def adjecent_nodes(point:tuple)->list:
    ret = []
    x,y = point
    if x != 0:
        ret.append((x - 1, y))
    if y != 0:
        ret.append((x, y - 1))
    if x < len(data[0]) - 1:
        ret.append((x + 1, y))
    if y < len(data) - 1:
        ret.append((x, y + 1))
    return ret

def path_sum(path):
    s = 0
    for node in path:
        s += cave[node[1]][node[0]]
    return s


def bfs_traverse_map(x,y,map):
    queue = []
    for node in adjecent_nodes((x,y)):
        queue.append([node, cave[node[1]][node[0]]])
        min_val[node[1]][node[0]] = cave[node[1]][node[0]]
    while True:
        if len(queue) == 0:
            break
        node, tmp_sum = queue.pop(0)
        for ad_node in adjecent_nodes(node):
            _x, _y = ad_node
            if tmp_sum + cave[_y][_x] < min_val[_y][_x]:
                queue.append([ad_node, tmp_sum + cave[_y][_x]])
                min_val[_y][_x] = tmp_sum + cave[_y][_x]



def extend(cave):
    l = list(range(10))
    ret = [[0]*(len(cave[0])*5) for _ in range(len(cave)*5)]
    for multi_x in range(5):
        for multi_y in range(5):
            for y in range(len(cave)):
                for x in range(len(cave[0])):
                    ret[y + multi_y*len(cave)][x + multi_x*len(cave[0])] = sum(list(map(int, list(str(cave[y][x] + multi_x + multi_y)))))
                    if ret[y + multi_y*len(cave)][x + multi_x*len(cave[0])] == 0: 
                        ret[y + multi_y*len(cave)][x + multi_x*len(cave[0])] = 1
    return ret

min_val = [[1<<32]*(len(data[0])*5) for _ in range(len(data)*5)]
extended_cave = extend(cave)
def adjecent_nodes_2(point:tuple)->list:
    ret = []
    x,y = point
    if x != 0:
        ret.append((x - 1, y))
    if y != 0:
        ret.append((x, y - 1))
    if x < len(extended_cave[0]) - 1:
        ret.append((x + 1, y))
    if y < len(extended_cave) - 1:
        ret.append((x, y + 1))
    return ret



def bfs_traverse_map_2(x,y):
    queue = []
    for node in adjecent_nodes((x,y)):
        queue.append([node, extended_cave[node[1]][node[0]]])
        min_val[node[1]][node[0]] = extended_cave[node[1]][node[0]]
    while True:
        if len(queue) == 0:
            break
        node, tmp_sum = queue.pop(0)
        for ad_node in adjecent_nodes_2(node):
            _x, _y = ad_node
            if tmp_sum + extended_cave[_y][_x] < min_val[_y][_x]:
                queue.append([ad_node, tmp_sum + extended_cave[_y][_x]])
                min_val[_y][_x] = tmp_sum + extended_cave[_y][_x]

bfs_traverse_map_2(0,0)
print(min_val[-1][-1])
for line in min_val:
    print(line)