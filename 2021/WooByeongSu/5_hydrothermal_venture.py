inputs = []
with open('input.txt', 'r') as f:
    inputs = f.readlines()

max_x = 0
max_y = 0
start = []
end = []
for line in inputs:
    line = line.split()
    start.append([int(num) for num in line[0].split(',')])
    end.append([int(num) for num in line[2].split(',')])

    if max_x < start[-1][0]:
        max_x = start[-1][0]
    if max_x < end[-1][0]:
        max_x = end[-1][0]
    if max_y < start[-1][1]:
        max_y = start[-1][1]
    if max_y < end[-1][1]:
        max_y = end[-1][1]
    
def is_horizontal(start, end):
    return start[1] == end[1]

def is_vertical(start, end):
    return start[0] == end[0]

def is_diagonal(start, end):
    return abs(start[0] - end[0]) == abs(start[1] - end[1])

def ascending_order(a, b):
    if a < b:
        return a, b
    else:
        return b, a

# part 1

board = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]

for i in range(len(start)):
    if is_horizontal(start[i], end[i]):
        _start, _end = ascending_order(start[i][0], end[i][0])
        for j in range(_start, _end + 1):
            board[j][start[i][1]] += 1
    elif is_vertical(start[i], end[i]):
        _start, _end = ascending_order(start[i][1], end[i][1])
        for j in range(_start, _end + 1):
            board[start[i][0]][j] += 1

cnt = 0
for i in board:
    for j in i:
        if j > 1:
            cnt += 1

print(cnt)

# part 2

for i in range(len(start)):
    if is_diagonal(start[i], end[i]):
        diff = [int((end[i][0] - start[i][0]) / abs(end[i][0] - start[i][0])), int((end[i][1] - start[i][1]) / abs(end[i][1] - start[i][1]))]
        cur = start[i]
        while cur != end[i]:
            board[cur[0]][cur[1]] += 1
            cur[0] += diff[0]
            cur[1] += diff[1]
        board[cur[0]][cur[1]] += 1

cnt = 0
for i in board:
    for j in i:
        if j > 1:
            cnt += 1

print(cnt)