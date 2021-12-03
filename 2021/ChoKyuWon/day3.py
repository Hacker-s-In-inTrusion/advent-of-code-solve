from aocd import data
from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=3)
res = 0
data = puzzle.input_data.split("\n")

def part1(data):
    gamma_rate = 0
    epsilon_rate = 0
    bit_length = len(data[0])
    for i in range(bit_length - 1, -1, -1):
        count0 = 0
        count1 = 1
        for j in data:
            if j[i] == "0":
                count0 += 1
            else:
                count1 += 1
        if count1 > count0:
            gamma_rate += (1<<bit_length - i - 1)
        else:
            epsilon_rate += (1<<bit_length - i - 1)
    
    print(gamma_rate * epsilon_rate)


def part2(data):
    return None

# data = """00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010""".split('\n')
print(part1(data), part2(data))