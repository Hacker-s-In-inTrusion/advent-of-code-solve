trench_range = [[70, 125], [-159, -121]]


def inbound(point):
    if trench_range[0][1] < point[0]:
        return False
    if trench_range[1][0] > point[1]:
        return False
    else:
        return True


def d17_part1():
    max_y = 0
    for velocity_x in range(0, 1000):
        for velocity_y in range(-1000, 1000):
            step_point = [0, 0]
            velocity = [velocity_x, velocity_y]
            ind_max_y = 0
            in_target = False
            while inbound(step_point):
                step_point[0] += velocity[0]
                step_point[1] += velocity[1]
                if velocity[0] > 0:
                    velocity[0] -= 1
                velocity[1] -= 1
                if step_point[1] > ind_max_y:
                    ind_max_y = step_point[1]
                if trench_range[0][0] <= step_point[0] <= trench_range[0][1]\
                   and trench_range[1][0] <= step_point[1] <= trench_range[1][1]:
                    in_target = True
                    break
            if in_target and ind_max_y > max_y:
                max_y = ind_max_y
    return max_y


def d17_part2():
    res = 0
    for velocity_x in range(0, 1000):
        for velocity_y in range(-1000, 1000):
            step_point = [0, 0]
            velocity = [velocity_x, velocity_y]
            ind_max_y = 0
            in_target = False
            while inbound(step_point):
                step_point[0] += velocity[0]
                step_point[1] += velocity[1]
                if velocity[0] > 0:
                    velocity[0] -= 1
                velocity[1] -= 1
                if step_point[1] > ind_max_y:
                    ind_max_y = step_point[1]
                if trench_range[0][0] <= step_point[0] <= trench_range[0][1]\
                   and trench_range[1][0] <= step_point[1] <= trench_range[1][1]:
                    in_target = True
                    break
            if in_target:
                res += 1
    return res


# def read_file():
#     input_file = open("input_day16.txt")
#     input_line = input_file.readline().rstrip()
#     output = [[70, 129], [-159, -121]]
#     return output


if __name__ == "__main__":
    # d16_input = read_file()
    part1 = d17_part1()
    print("answer of part 1: %d" % part1)
    part2 = d17_part2()
    print("answer of part 2: %d" % part2)
