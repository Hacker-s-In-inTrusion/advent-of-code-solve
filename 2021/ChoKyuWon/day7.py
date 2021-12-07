from aocd import data
from aocd.models import Puzzle

def fuel_cost(n):
    if PART2: return int(n*(n+1)/2)
    else: return n

def calc_cost(data, pivot):
    cost = 0
    for i in data:
        cost += fuel_cost(abs(pivot - i))
    return cost


puzzle = Puzzle(year=2021, day=7)
input_str = puzzle.input_data
# input_str = "16,1,2,0,4,2,7,1,2,14"
data = list(map(int,input_str.split(",")))

PART2 = True
cost = 1<<64 - 1
for i in range(max(data)):
    _cost = calc_cost(data, i)
    if cost > _cost:
        cost = _cost

print(cost)