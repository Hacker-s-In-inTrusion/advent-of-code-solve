board = []
with open('input.txt', 'r') as f:
    while True:
        temp = f.readline()
        if not temp:
            break
        board.append([int(n) for n in temp[:-1]])

y_len = len(board)
x_len = len(board[0])

# part 1

result = 0

for x in range(x_len):
    for y in range(y_len):
        left = max(x - 1, 0)
        right = min(x + 1, x_len - 1)
        up = max(y - 1, 0)
        down = min(y + 1, y_len - 1)

        if left != x and board[y][left] <= board[y][x]:
            continue
        if right != x and board[y][right] <= board[y][x]:
            continue
        if up != y and board[up][x] <= board[y][x]:
            continue
        if down != y and board[down][x] <= board[y][x]:
            continue

        result += (board[y][x] + 1)


print(result)

# part 2

def basin(board, y, x, history):
    size = 1
    history.append((x, y))
    left = max(x - 1, 0)
    right = min(x + 1, x_len - 1)
    up = max(y - 1, 0)
    down = min(y + 1, y_len - 1)

    if left != x and board[y][left] > board[y][x] and board[y][left] != 9 and (left, y) not in history:
        temp_size, history = basin(board, y, left, history)
        size += temp_size
    if right != x and board[y][right] > board[y][x] and board[y][right] != 9 and (right, y) not in history:
        temp_size, history = basin(board, y, right, history)
        size += temp_size
    if up != y and board[up][x] > board[y][x] and board[up][x] != 9 and (x, up) not in history:
        temp_size, history = basin(board, up, x, history)
        size += temp_size
    if down != y and board[down][x] > board[y][x] and board[down][x] != 9 and (x, down) not in history:
        temp_size, history = basin(board, down, x, history)
        size += temp_size

    return size, history

basin_size = []

for x in range(x_len):
    for y in range(y_len):
        basin_size.append(basin(board, y, x, [])[0])
basin_size.sort()

print(basin_size[-1] * basin_size[-2] * basin_size[-3])