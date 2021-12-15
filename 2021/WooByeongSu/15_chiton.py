import numpy as np

board = []
with open('asdf.txt', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        board.append([int(i) for i in line[:-1]])

np_board = np.array(board)
np_board_1 = np_board + 1
np_board_1[np_board_1 == 10] = 1
np_board_2 = np_board_1 + 1
np_board_2[np_board_2 == 10] = 1
np_board_3 = np_board_2 + 1
np_board_3[np_board_3 == 10] = 1
np_board_4 = np_board_3 + 1
np_board_4[np_board_4 == 10] = 1
np_board = np.concatenate((np_board, np_board_1, np_board_2, np_board_3, np_board_4), axis=1)

np_board_1 = np_board + 1
np_board_1[np_board_1 == 10] = 1
np_board_2 = np_board_1 + 1
np_board_2[np_board_2 == 10] = 1
np_board_3 = np_board_2 + 1
np_board_3[np_board_3 == 10] = 1
np_board_4 = np_board_3 + 1
np_board_4[np_board_4 == 10] = 1
np_board = np.concatenate((np_board, np_board_1, np_board_2, np_board_3, np_board_4), axis=0)

board = np_board.tolist()

x_len = len(board[0])
y_len = len(board)

history_x = [0]
history_y = [0]
target = 0
for i in range(1, x_len):
    layer_x = []
    layer_y = []
    for y in range(i):
        layer_y.append(board[y][i])
    for x in range(i):
        layer_x.append(board[i][x])

    new_history_x = []
    new_history_y = []
    '''
    for x in range(len(layer_x)):
        compare_list = [history_x[x]]
        for a in range(x):
            num = history_x[a]
            for b in range(a, x):
                num += layer_x[b]
            compare_list.append(num)
        for a in range(x + 1, len(layer_x)):
            num = history_x[a]
            for b in range(x + 1, a):
                num += layer_x[b]
            compare_list.append(num)
        
        for a in range(len(layer_y)):
            num = history_y[a]
            for b in range(a, len(layer_y)):
                num += layer_y[b]
            num += board[i][i]
            for b in range(x + 1, len(layer_x)):
                num += layer_x[b]
            compare_list.append(num)
        new_history_x.append(min(compare_list))
    
    for y in range(len(layer_y)):
        compare_list = [history_y[y]]
        for a in range(y):
            num = history_y[a]
            for b in range(a, y):
                num += layer_y[b]
            compare_list.append(num)
        for a in range(y + 1, len(layer_y)):
            num = history_y[a]
            for b in range(y + 1, a):
                num += layer_y[b]
            compare_list.append(num)
        
        for a in range(len(layer_y)):
            num = history_y[a]
            for b in range(a, len(layer_y)):
                num += layer_y[b]
            num += board[i][i]
            for b in range(y + 1, len(layer_y)):
                num += layer_y[b]
            compare_list.append(num)
        new_history_y.append(min(compare_list))
    '''
    
    if new_history_x[-1] < new_history_y[-1]:
        target = board[i][i] + new_history_x[-1]
    else:
        target = board[i][i] + new_history_y[-1]
    new_history_x.append(target)
    new_history_y.append(target)

    history_x = new_history_x
    history_y = new_history_y
    
print(target)



'''
distance = []
distance_len = x_len * y_len
for y in range(y_len):
    for x in range(x_len):
        d = [float("inf") for _ in range(distance_len)]
        idx = x + x_len * y
        horizontal_next = idx + 1
        vertical_next = idx + x_len
        horizontal_prev = idx - 1
        vertical_prev = idx - x_len
        d[idx] = 0
        if x + 1 < x_len:
            d[horizontal_next] = board[y][x + 1]
        if y + 1 < y_len:
            d[vertical_next] = board[y + 1][x]
        if x - 1 >= 0:
            d[horizontal_prev] = board[y][x - 1]
        if y - 1 >= 0:
            d[vertical_prev] = board[y - 1][x]
        distance.append(d)

visited = [False for _ in range(distance_len)]
d = distance[0]
visited[0] = True
cur = 1 if d[1] < d[1 + x_len] else 1 + x_len
while cur != distance_len - 1:
    visited[cur] = True
    cur_dist = distance[cur]
    length = d[cur]
    for i in range(len(d)):
        if visited[i]:
            continue
        if length + cur_dist[i] < d[i]:
            d[i] = length + cur_dist[i]
    minimum = float("inf")
    for i in range(len(d)):
        if visited[i]:
            continue
        if d[i] < minimum:
            minimum = d[i]
            cur = i

print(d[-1])
'''