from aocd.models import Puzzle

p = Puzzle(2021, 10)
input_str = p.input_data
# input_str="""[({(<(())[]>[[{[]{<()<>>
# [(()[<>])]({[<{<<[]>>(
# {([(<{}[<>[]}>{[]{[(<()>
# (((({<>}<{<{<>}{[]{[]{}
# [[<[([]))<([[{}[[()]]]
# [{[{({}]{}}([{[{{{}}([]
# {<[[]]>}<{[{[{[]{()[[[]
# [<(<(<(<{}))><([]([]()
# <{([([[(<>()){}]>(<<{{
# <{([{{}}[<[[[<>{}]]]>[]]"""

data = input_str.split("\n")

brace_open = ["(", "{", "[", "<"]
brace_pair = {"(":")", "{":"}", "[":"]", "<":">"}
brace_score = {")":3, "]":57, "}":1197, ">":25137}

# Part 1
score = 0
for line in data:
    stack = []
    for ch in line:
        if ch in brace_open:
            stack.append(ch)
        else:
            pos = stack.pop()
            if ch != brace_pair[pos]:
                score += brace_score[ch]
                break
print(score)
# Part 2
brace_score = {")":1, "]":2, "}":3, ">":4}
def calc_score(s:str) -> int:
    score = 0
    for ch in s:
        score *= 5
        score += brace_score[ch]
    return score
def incomplete(stack:list)->int:
    s = ""
    while True:
        if len(stack) == 0:
            return calc_score(s)
        s += brace_pair[stack.pop()]

score = []
for line in data:
    stack = []
    flag = True
    for ch in line:
        if ch in brace_open:
            stack.append(ch)
        else:
            pos = stack.pop()
            if ch != brace_pair[pos]:
                flag = False
                break
    if flag: score.append(incomplete(stack))
print(sorted(score)[int(len(score)/2)])