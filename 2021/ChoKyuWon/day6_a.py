class LanternFish():
    def __init__(self, timer):
        self.timer = timer
    def count(self):
        child = None
        self.timer -= 1
        if self.timer == -1:
            child = LanternFish(8)
            self.timer = 6
        return child

from aocd import data
from aocd.models import Puzzle

def main():
    puzzle = Puzzle(year=2021, day=6)
    data = puzzle.input_data.split(",")
    # data = "3,4,3,1,2".split(",")
    data = list(map(int, data))
    school = [LanternFish(i) for i in data]
    for i in range(1, 257):
        childs = []
        for fish in school:
            child = fish.count()
            if child is not None : childs.append(child)
        school += childs
    print(len(school))
        

main()