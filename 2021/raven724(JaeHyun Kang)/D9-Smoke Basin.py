check_location = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def d9_part1(map):
    len_x = len(map)
    len_y = len(map[0])
    res = 0
    basin_point = []
    for i in range(len_x):
        for j in range(len_y):
            is_lowest = True
            for a in check_location:
                new_x = i + a[0]
                new_y = j + a[1]
                if new_x < 0 or new_x >= len_x:
                    continue
                elif new_y < 0 or new_y >= len_y:
                    continue
                else:
                    if map[new_x][new_y] <= map[i][j]:
                        is_lowest = False
                        break
            if is_lowest:
                basin_point.append([i, j])
                res += int(map[i][j]) + 1
    return res, basin_point


def d9_part2(map, point):
    res = []
    len_x = len(map)
    len_y = len(map[0])
    for ind_point in point:
        if map[ind_point[0]][ind_point[1]] == '9':
            continue
        else:
            count = 0
            stack_point = []
            stack_point.append(ind_point)
            while len(stack_point) > 0:
                cur_point = stack_point.pop()
                if map[cur_point[0]][cur_point[1]] == '9':
                    continue
                count += 1
                for a in check_location:
                    new_x = cur_point[0] + a[0]
                    new_y = cur_point[1] + a[1]
                    if new_x < 0 or new_x >= len_x:
                        continue
                    elif new_y < 0 or new_y >= len_y:
                        continue
                    else:
                        if map[new_x][new_y] > map[cur_point[0]][cur_point[1]]\
                         and map[new_x][new_y] != '9':
                            stack_point.append([new_x, new_y])
                map[cur_point[0]][cur_point[1]] = '9'
            res.append(count)
    res.sort(reverse=True)
    return res


def read_file():
    input_file = open("input_smoke.txt")
    input_line = input_file.readline().strip()
    output = []
    while input_line:
        output.append(list(input_line))
        input_line = input_file.readline().strip()
    return output


if __name__ == "__main__":
    map_input = read_file()
    part1, basin_point = d9_part1(map_input)
    print("answer of part 1: %d" % part1)
    res = d9_part2(map_input, basin_point)
    part2 = 1
    for i in res[:3]:
        part2 *= i
    print("answer of part 2: %d" % part2)
