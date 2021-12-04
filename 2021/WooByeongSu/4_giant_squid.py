inputs = None
board = []
with open('./input.txt', 'r') as f:
    inputs = [int(num) for num in f.readline().split(',')]
    f.readline()
    for _ in range(100):
        game_board = []
        for _ in range(5):
            game_board.append([int(num) for num in f.readline().split()])
        board.append(game_board)
        f.readline()

flag_board = []
for _ in range(100):
    flag_board.append([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

def is_winner(flag_board, pos):
    '''
    case = 1
    left_diagonal = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]
    right_diagonal = [[0, 4], [1, 3], [2, 2], [3, 1], [4, 0]]
    if pos == [2, 2]:
        case = 2
    elif pos[0] == pos[1]: # left_diagonal
        case = 3
    elif pos[0] + pos[1] == 4: # right_diagonal
        case = 4

    if case == 2 or case == 3:
        cnt = 0
        for i, j in left_diagonal:
            if flag_board[i][j] == 1:
                cnt += 1
        if cnt == 5:
            return True
    
    if case == 2 or case == 4:
        cnt = 0
        for i, j in right_diagonal:
            if flag_board[i][j] == 1:
                cnt += 1
        if cnt == 5:
            return True
    '''
    cnt = 0
    for i in range(5):
        if flag_board[pos[0]][i] == 1:
            cnt += 1
    if cnt == 5:
        return True
    
    cnt = 0
    for i in range(5):
        if flag_board[i][pos[1]] == 1:
            cnt += 1
    if cnt == 5:
        return True
    
    return False

last_input = []
win_board_num = []
win_board = []
win_flag_board = []

for num in inputs:
    for i in range(len(board)):
        if i in win_board_num:
            continue

        for a in range(5):
            for b in range(5):
                if num == board[i][a][b]:
                    flag_board[i][a][b] = 1
                    if is_winner(flag_board[i], [a, b]):
                        last_input.append(num)
                        win_board_num.append(i)
                        win_board.append(board[i])
                        win_flag_board.append(flag_board[i])

sum = 0
for a in range(5):
    for b in range(5):
        if win_flag_board[0][a][b] == 0:
            sum += win_board[0][a][b]

print(last_input[0] * sum)

sum = 0
for a in range(5):
    for b in range(5):
        if win_flag_board[-1][a][b] == 0:
            sum += win_board[-1][a][b]

print(last_input[-1] * sum)