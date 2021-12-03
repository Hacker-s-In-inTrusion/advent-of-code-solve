from aocd import data
from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=2)
res = 0
data = puzzle.input_data.split("\n")

def part1(data):
    pos_x = 0
    pos_y = 0

    for s in data:
        tmp = s.split(' ')
        if tmp[0] == "forward":
            pos_x += int(tmp[1])
        elif tmp[0] == "down":
            pos_y += int(tmp[1])
        elif tmp[0] == "up":
            pos_y -= int(tmp[1])
    
    return pos_x * pos_y

def part2(data):
    pos_x = 0
    pos_y = 0
    aim = 0
    for s in data:
        tmp = s.split(' ')
        if tmp[0] == "forward":
            pos_x += int(tmp[1])
            pos_y += int(tmp[1]) * aim
        elif tmp[0] == "down":
            aim += int(tmp[1])
        elif tmp[0] == "up":
            aim -= int(tmp[1])
    
    return pos_x * pos_y

print(part1(data), part2(data))