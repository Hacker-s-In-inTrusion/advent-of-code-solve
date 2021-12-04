number_order = None
bingo_board = []
mark_bingo = []
score_bingo = []
num_board = 0


def check_bingo(number):
    for index_board in range(num_board):
        ind_bingo = bingo_board[index_board]
        if ind_bingo[0][0] == -2:
            continue
        for i in range(5):
            row_bingo = True
            col_bingo = True
            for j in range(5):
                if col_bingo is True and ind_bingo[i][j] != -1:
                    col_bingo = False
                if row_bingo is True and ind_bingo[j][i] != -1:
                    row_bingo = False
            if row_bingo or col_bingo:
                num_left = 0
                for i in range(5):
                    num_left += sum(ind_bingo[i]) + ind_bingo[i].count(-1)
                score_bingo.append(num_left * number)
                ind_bingo[0][0] = -2
                break


def mark_number(number):
    for ind_bingo in bingo_board:
        for i in range(5):
            for j in range(5):
                if ind_bingo[i][j] == number:
                    ind_bingo[i][j] = -1


if __name__ == "__main__":
    input_file = open("input.txt", "r")
    number_order = list(map(int, input_file.readline().split(',')))
    _ = input_file.readline()
    while True:
        ind_bingo = []
        ind_line = list(map(int, input_file.readline().split()))
        if ind_line:
            ind_bingo.append(ind_line)
            for _ in range(4):
                ind_bingo.append(list(map(int, input_file.readline().split())))
            _ = input_file.readline()
            bingo_board.append(ind_bingo)
        else:
            break
    num_board = len(bingo_board)
    for num in number_order:
        mark_number(num)
        check_bingo(num)
    print(score_bingo)  # Print score for all bingo boards as order.
