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
        bit = 0 if count0>count1 else 1
        gamma_rate += (bit<<bit_length - i - 1)
    
    mask = (1 << bit_length) - 1
    epsilon_rate = gamma_rate ^ mask
    return gamma_rate * epsilon_rate


def part2(data):
    oxy_rate = 0
    co2_rate = 0
    bit_length = len(data[0])
    oxy_pruned_list = data
    co2_pruned_list = data
    for i in range(bit_length):
        count0 = 0
        count1 = 0
        for j in oxy_pruned_list:
            if j[i] == "0":
                count0 += 1
            else:
                count1 += 1
        bit = 0 if count0>count1 else 1

        _oxy_pruned_list = []
        for node in oxy_pruned_list:
            if int(node[i]) == bit:
                _oxy_pruned_list.append(node)
        if len(_oxy_pruned_list) == 1:
            oxy_rate += int(_oxy_pruned_list[0][i:], 2)
            break
        oxy_pruned_list = _oxy_pruned_list
        oxy_rate += (bit<<bit_length - i - 1)

    for i in range(bit_length):
        count0 = 0
        count1 = 0
        for j in co2_pruned_list:
            if j[i] == "0":
                count0 += 1
            else:
                count1 += 1
        bit = 0 if count0<=count1 else 1

        _co2_pruned_list = []
        for node in co2_pruned_list:
            if int(node[i]) == bit:
                _co2_pruned_list.append(node)
        if len(_co2_pruned_list) == 1:
            print("Break!", i, _co2_pruned_list[0])
            co2_rate += int(_co2_pruned_list[0][i:], 2)
            break
        co2_pruned_list = _co2_pruned_list
        co2_rate += (bit<<bit_length - i - 1)
    print(oxy_rate, co2_rate)
    return oxy_rate * co2_rate

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