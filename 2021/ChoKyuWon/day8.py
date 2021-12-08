from aocd import data
from aocd.models import Puzzle

def atobit(ch)->int:
    return int("1"+"0"*(ord(ch) - ord('a')), 2)

def countone(num:int)->int:
    str()
class Segments:
    def __init__(self, str):
        self.mapping = {}
        inputs = sorted(str[:-1].split(" "), key=lambda x:len(x))
        input_bitmap = [0]*10
        for index, input in enumerate(inputs):
            for ch in sorted(input):
                input_bitmap[index] += atobit(ch)
        self._gen_map(input_bitmap)

    def relocation(self, alphabet):
        bits = 0
        for ch in alphabet:
            bits |= atobit(ch)
        return self.mapping[bits]
    def alloc(self, bitmap, digit):
        self.mapping[bitmap] = digit
    
    def reverse_map(self, digit):
        return list(self.mapping.keys())[list(self.mapping.values()).index(digit)]
    def _gen_map(self, bitmap):
        self.mapping[bitmap[0]] = 1
        self.mapping[bitmap[1]] = 7
        self.mapping[bitmap[2]] = 4
        self.mapping[bitmap[-1]] = 8
        for len_5 in bitmap[3:6]:
            if len_5 & self.reverse_map(1) == self.reverse_map(1):
                self.mapping[len_5] = 3
            elif bin(len_5 & self.reverse_map(4))[1:].count('1') == 2:
                self.mapping[len_5] = 2
            else:
                self.mapping[len_5] = 5

        for len_6 in bitmap[6:9]:
            if len_6 & self.reverse_map(4) == self.reverse_map(4):
                self.mapping[len_6] = 9
            elif len_6 & self.reverse_map(1) == self.reverse_map(1):
                self.mapping[len_6] = 0
            else:
                self.mapping[len_6] = 6

puzzle = Puzzle(year=2021, day=8)
input_str = puzzle.input_data
# input_str="""be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
# edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
# fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
# fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
# aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
# fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
# dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
# bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
# egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
# gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

part1_score = 0
part2_score = 0
data = input_str.split("\n")
for d in data:
    outputs = d.split("|")[1]
    seg = Segments(d.split("|")[0])
    s = ""
    for output in outputs[1:].split(" "):
        out = seg.relocation(output)
        if out in [1,4,7,8]:
            part1_score += 1
        s += str(out)
    part2_score += int(s)

print(part1_score, part2_score)