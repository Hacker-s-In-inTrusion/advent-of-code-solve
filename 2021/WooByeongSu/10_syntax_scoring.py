import numpy as np

def calculate_complete_score(stack):
    complete_score = 0
    stack.reverse()
    for c in stack:
        if c == "(":
            complete_score = complete_score * 5 + 1
        elif c == "{":
            complete_score = complete_score * 5 + 3
        elif c == "<":
            complete_score = complete_score * 5 + 4
        elif c == "[":
            complete_score = complete_score * 5 + 2
    return complete_score

syntax_score = 0
complete_score = []
with open('input.txt', 'r') as f:
    while True:
        temp = f.readline()
        if not temp:
            break
        temp = temp[:-1]
        stack = []
        flag = True
        for i in temp:
            if i == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    syntax_score += 3
                    flag = False
                    break
            elif i == "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    syntax_score += 1197
                    flag = False
                    break
            elif i == ">":
                if stack and stack[-1] == "<":
                    stack.pop()
                else:
                    syntax_score += 25137
                    flag = False
                    break
            elif i == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    syntax_score += 57
                    flag = False
                    break
            else:
                stack.append(i)

        if flag:
            complete_score.append(calculate_complete_score(stack))

print(syntax_score)

np_arr = np.array(complete_score)
print(int(np.median(np_arr)))