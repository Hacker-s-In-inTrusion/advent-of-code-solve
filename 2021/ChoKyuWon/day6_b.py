class School():
    def __init__(self, data):
        self.list = [0]*9
        for d in data:
            self.list[d] += 1
    def count(self):
        new_list = [0]*9
        for i in range(0,8):
            new_list[i] = self.list[i + 1]
        new_list[8] = self.list[0]
        new_list[6] += self.list[0]
        self.list = new_list
    def solve(self):
        return sum(self.list)

from aocd import data
from aocd.models import Puzzle

def main():
    puzzle = Puzzle(year=2021, day=6)
    data = puzzle.input_data.split(",")
    # data = "3,4,3,1,2".split(",")
    data = sorted(list(map(int, data)))
    school = School(data)
    for _ in range(256):
        school.count()
    print(school.solve())
        

main()