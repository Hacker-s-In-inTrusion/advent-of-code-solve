from collections import Counter

template = None
command = []
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
        command.append(line[0])

for i in range(len(template) - 1):
    for cmd in command:
        if template[i:i+2] == cmd:
            command_list.append(cmd)

for _ in range(40):
    new_command_list = []
    for cmd in command_list:
        new_str = cmd[0] + command_pair[cmd] + cmd[1]
        new_command_list.append(new_str[0:2])
        new_command_list.append(new_str[1:3])
    command_list = new_command_list

print(command_list)
