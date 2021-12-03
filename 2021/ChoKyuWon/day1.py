from aocd import data
from aocd.models import Puzzle

def part2(data):
    window = []
    for i in range(len(data) - 2):
        window.append(data[i] + data[i+1] + data[i+2])
    return count_increased_num(window)

def part1(data):
    return count_increased_num(data)

def count_increased_num(data):
    res = 0
    for (index, num) in enumerate(data):
        if index == 0 :
            continue
        if num > data[index - 1]:
            res += 1
    return res

puzzle = Puzzle(year=2021, day=1)
res = 0
str_data = puzzle.input_data.split("\n")
data = []

for node in str_data:
    data.append(int(node))

print(part1(data))
print(part2(data))
