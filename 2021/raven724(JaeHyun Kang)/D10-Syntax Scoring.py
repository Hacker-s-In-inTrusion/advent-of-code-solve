list_open = ['(', '[', '{', '<']
list_close = [')', ']', '}', '>']
list_point_corrupt = [3, 57, 1197, 25137]
list_point_incomplete = [1, 2, 3, 4]


def d10_part1(data):
    res_point = 0
    res_corrupt = []
    for ind_index, ind_data in enumerate(data):
        stack_key = []
        for i in ind_data:
            if i in list_open:
                stack_key.append(i)
            else:
                index_close = list_close.index(i)
                index_open = list_open.index(stack_key.pop())
                if index_close != index_open:
                    res_point += list_point_corrupt[index_close]
                    res_corrupt.append(ind_index)
                    break
    return res_point, res_corrupt


def d10_part2(data, corrupt):
    res_point = []
    for ind_index, ind_data in enumerate(data):
        ind_res_point = 0
        if ind_index in corrupt:
            continue
        stack_key = []
        for i in ind_data:
            if i in list_open:
                stack_key.append(i)
            else:
                _ = stack_key.pop()
        stack_key.reverse()
        for i in stack_key:
            index_element = list_open.index(i)
            ind_res_point =\
                ind_res_point * 5 + list_point_incomplete[index_element]
        res_point.append(ind_res_point)
    res_point.sort()
    half = len(res_point) // 2
    return res_point[half]


def read_file():
    input_file = open("../input/input_day10.txt")
    input_line = input_file.readline().rstrip()
    output = []
    while input_line:
        output.append(list(input_line))
        input_line = input_file.readline().rstrip()
    return output


if __name__ == "__main__":
    day10_input = read_file()
    part1, list_currupt = d10_part1(day10_input)
    print("answer of part 1: %d" % part1)
    part2 = d10_part2(day10_input, list_currupt)
    print("answer of part 2: %d" % part2)
