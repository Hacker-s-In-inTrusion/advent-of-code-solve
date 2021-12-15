from collections import Counter

template = None
command_list = []
command_pair = {}

with open('input.txt', 'r') as f:
    template = f.readline()[:-1]
    f.readline()
    while True:
        line = f.readline()
        if not line:
            break
        line = line[:-1].split()
        command_pair[line[0]] = line[2]

for i in range(len(template) - 1):
    cmd = template[i:i + 2]
    command_list.append(cmd)
c = dict(Counter(command_list))

for _ in range(40):
    new_c = {}
    for cmd in c:
        new_char = command_pair[cmd]
        new_cmd_1 = cmd[0] + new_char
        new_cmd_2 = new_char + cmd[1]
        if new_cmd_1 in new_c:
            new_c[new_cmd_1] += c[cmd]
        else:
            new_c[new_cmd_1] = c[cmd]
        if new_cmd_2 in new_c:
            new_c[new_cmd_2] += c[cmd]
        else:
            new_c[new_cmd_2] = c[cmd]
    c = new_c

elements = {}
for i in c:
    for char in i:
        if char in elements:
            elements[char] += c[i]
        else:
            elements[char] = c[i]

for i in elements:
    elements[i] //= 2

maximum = 0
for i in elements:
    if elements[i] > maximum:
        maximum = elements[i]

minimum = maximum
for i in elements:
    if elements[i] < minimum:
        minimum = elements[i]

print(maximum - minimum)
