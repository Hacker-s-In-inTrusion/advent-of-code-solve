def d2_part1(cmd):
    depth = 0
    x_position = 0
    for ind_cmd in cmd:
        if ind_cmd[0] == "forward":
            x_position += int(ind_cmd[1])
        elif ind_cmd[0] == "down":
            depth += int(ind_cmd[1])
        elif ind_cmd[0] == "up":
            depth -= int(ind_cmd[1])
    return depth * x_position


def d2_part2(cmd):
    depth = 0
    x_position = 0
    aim = 0
    for ind_cmd in cmd:
        if ind_cmd[0] == "forward":
            x_position += int(ind_cmd[1])
            depth += aim * int(ind_cmd[1])
        elif ind_cmd[0] == "down":
            aim += int(ind_cmd[1])
        elif ind_cmd[0] == "up":
            aim -= int(ind_cmd[1])
    return depth * x_position


def read_file():
    input_file = open("../input/input_day2.txt")
    input_line = input_file.readline().rstrip('')
    output = []
    while input_line:
        output.append(input_line.split())
        input_line = input_file.readline().rstrip()
    return output


if __name__ == "__main__":
    cmd_input = read_file()
    part1 = d2_part1(cmd_input)
    print("answer of part 1: %d" % part1)
    part2 = d2_part2(cmd_input)
    print("answer of part 2: %d" % part2)
