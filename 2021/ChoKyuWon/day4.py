from aocd import data
from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=4)
res = 0
data = puzzle.input_data.split("\n\n")

# data = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19

#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7""".split("\n\n")

call_number = data[0].split(",")
boards = data[1:]


board_length = len(boards[0].split('\n'))
marked_board = []
for _ in range(len(boards)):
    marked_board.append([])

def find_number(num, board):
    for x_index, x in enumerate(board.split("\n")):
        blank_count = 0
        for y_index, y in enumerate(x.split(" ")):
            if y == '': 
                blank_count +=1
                continue
            if int(y.strip()) == num:
                return (x_index,y_index - blank_count)
    return None

def win(marked_board, board_length):
    for i in range(board_length):
        count_x = 0
        count_y = 0
        for mark in marked_board:
            if mark[0] == i: count_x += 1
            if mark[1] == i: count_y += 1
        if (count_x == board_length) or (count_y == board_length):
            return True

    return False

def calc_score(board, marked_board):
    array = []
    for x in board.split("\n"):
        for y in x.split(" "):
            if y == "": continue
            array.append(int(y))

    for mark in marked_board:
        index = mark[0] * len(board.split("\n")) + mark[1]
        array[index] = 0
    return sum(array)

score = 0
windex = -1

## part 1
for num in call_number:
    for index, board in enumerate(boards):
        found = find_number(int(num), board)
        if found is not None:
            marked_board[index].append(found)
            if win(marked_board[index], board_length) == True:
                score = calc_score(board, marked_board[index])
                print(score * int(num))
    if score > 0 :break

## part 2
solved_index = []
marked_board = []
for _ in range(len(boards)):
    marked_board.append([])

for num in call_number:
    for index, board in enumerate(boards):
        if index in solved_index:
            continue
        found = find_number(int(num), board)
        if found is not None:
            marked_board[index].append(found)
            if win(marked_board[index], board_length) == True:
                tmp = calc_score(board, marked_board[index])
                solved_index.append(index)
                if len(solved_index) == len(boards):
                    print( tmp * int(num))
