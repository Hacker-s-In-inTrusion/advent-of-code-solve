import copy

dots_x = []
dots_y = []
command = []
with open('input.txt', 'r') as f:
    while True:
        line = f.readline()
        if line == "\n":
            break
        line = line[:-1].split(',')
        dots_x.append(int(line[0]))
        dots_y.append(int(line[1]))
    while True:
        line = f.readline()
        if not line:
            break
        cmd = line.split()[2]
        cmd = cmd.split('=')
        command.append([cmd[0], int(cmd[1])])

paper = [[False for _ in range(max(dots_x) + 1)] for _ in range(max(dots_y) + 1)]

for i in range(len(dots_x)):
    paper[dots_y[i]][dots_x[i]] = True

for cmd, num in command:
    temp = copy.deepcopy(paper)
    new_paper = None
    if cmd == 'x':
        for i in range(len(temp)):
            temp[i].reverse()
        new_paper = [[False for _ in range(num)] for _ in range(len(temp))]
    else:
        temp.reverse()
        new_paper = [[False for _ in range(len(temp[0]))] for _ in range(num)]
    
    for x in range(len(new_paper[0])):
        for y in range(len(new_paper)):
            new_paper[y][x] = paper[y][x] or temp[y][x]
    
    temp = None
    paper = new_paper

    # part 1
    # break

# part 1
# cnt = 0
# for x in paper:
#     cnt += x.count(True)
# print(cnt)

# part 2
for y in paper:
    for x in y:
        if x:
            print("#",end='')
        else:
            print(".",end='')
    print("")
