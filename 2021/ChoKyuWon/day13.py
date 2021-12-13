from os import path
from aocd.models import Puzzle
p = Puzzle(2021, 13)
input_str = p.input_data
# input_str="""6,10
# 0,14
# 9,10
# 0,3
# 10,4
# 4,11
# 6,0
# 6,12
# 4,1
# 0,13
# 10,12
# 3,4
# 3,0
# 8,4
# 1,10
# 2,14
# 8,10
# 9,0

# fold along y=7
# fold along x=5"""

inital_dots = input_str.split("\n\n")[0].split("\n")
folds = input_str.split("\n\n")[1].split("\n")
x_flag = False
y_flag = False

for f in folds:
    if "x" in f and x_flag == False:
        x_flag = True
        max_x = int(f.split('=')[1]) * 2 + 1
    if "y" in f and y_flag == False:
        y_flag = True
        max_y = int(f.split('=')[1]) * 2 + 1
    if x_flag and y_flag:
        break

paper = [[0]*max_x for _ in range(max_y)]

for dot in inital_dots:
    x = int(dot.split(",")[0])
    y = int(dot.split(",")[1])
    paper[y][x] = 1

def fold(paper:list, line:int, x:bool)->list:
    if x:
        folded_paper = [[0]*(int(len(paper[0])/2)) for _ in range(len(paper))]
        for y in range(len(paper)):
            for x in range(line):
                folded_paper[y][x] |= paper[y][x]
                folded_paper[y][x] |= paper[y][2*line - x]
        
    else:
        folded_paper = [[0]*int(len(paper[0])) for _ in range(int(len(paper)/2))]
        for x in range(len(paper[0])):
            for y in range(line):
                folded_paper[y][x] |= paper[y][x]
                folded_paper[y][x] |= paper[2*line - y][x]

    return folded_paper

new_paper = paper
for index, insn in enumerate(folds):
    num = int(insn.split("=")[1])
    x = True if "x" in insn else False
    new_paper = fold(new_paper, num, x)
    # Part 1
    if index == 0:
        count_dots = sum([sum(map(lambda x: x==1, o)) for o in new_paper])
        print(count_dots)
# Part 2
for line in new_paper:
    print(line)



