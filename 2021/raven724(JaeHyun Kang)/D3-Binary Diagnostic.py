def d3_part1(data):
    len_data = len(data)
    len_inddata = len(data[0])
    gamma = '0b'
    epsilon = '0b'
    for i in range(len_inddata):
        num_0 = 0
        num_1 = 0
        for j in range(len_data):
            if data[j][i] == '1':
                num_1 += 1
            else:
                num_0 += 1
        if num_0 > num_1:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    return int(gamma, 2) * int(epsilon, 2)


def check_bit(data, bit, list):
    res_0 = []
    res_1 = []
    for a in list:
        if data[a][bit] == '0':
            res_0.append(a)
        else:
            res_1.append(a)
    return res_0, res_1


def d3_part2(data):
    oxygen = []
    co2 = []
    list_use_data = list(range(len(data)))
    list_0, list_1 = check_bit(data, 0, list_use_data)
    if len(list_0) > len(list_1):
        oxygen = list_0
        co2 = list_1
    else:
        oxygen = list_1
        co2 = list_0
    for i in range(1, len(data[0])):
        if len(oxygen) == 1:
            break
        list_0, list_1 = check_bit(data, i, oxygen)
        if len(list_0) > len(list_1):
            oxygen = list_0
        else:
            oxygen = list_1
    for i in range(1, len(data[0])):
        if len(co2) == 1:
            break
        list_0, list_1 = check_bit(data, i, co2)
        if len(list_0) > len(list_1):
            co2 = list_1
        else:
            co2 = list_0
    print(oxygen)
    print(co2)
    str_oxygen = '0b' + ''.join(data[oxygen[0]])
    str_co2 = '0b' + ''.join(data[co2[0]])
    return int(str_oxygen, 2) * int(str_co2, 2)


def read_file():
    input_file = open("../input/input_day3.txt")
    input_line = input_file.readline().rstrip()
    output = list()
    while input_line:
        output.append(list(input_line))
        input_line = input_file.readline().rstrip()
    return output


if __name__ == "__main__":
    data_input = read_file()
    part1 = d3_part1(data_input)
    print("answer of part 1: %d" % part1)
    part2 = d3_part2(data_input)
    print("answer of part 2: %d" % part2)
