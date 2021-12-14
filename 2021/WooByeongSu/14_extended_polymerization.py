from collections import Counter

template = {}
command = {}
command_num = {}

with open('input.txt', 'r') as f:
    line = f.readline()[:-1]
    for i in range(len(line)):
        template[i] = line[i]
    f.readline()
    while True:
        line = f.readline()
        if not line:
            break
        line = line[:-1].split()
        command[line[0]] = line[2]
        command_num[line[0]] = 0

for _ in range(10):
    add_template = {}
    for i in range(len(template) - 1):
        cur = template[i] + template[i + 1]
        if cur in command:
            add_template[i + 0.5] = command[cur]
    
    new_template = {}
    template_keys = list(template.keys())
    add_template_keys = list(add_template.keys())
    i = 0
    template_keys_idx = 0
    add_template_keys_idx = 0

    while template_keys_idx < len(template_keys) or add_template_keys_idx < len(add_template_keys):
        if template_keys_idx >= len(template_keys):
            new_template[i] = add_template[add_template_keys[add_template_keys_idx]]
            i += 1
            add_template_keys_idx += 1
        elif add_template_keys_idx >= len(add_template_keys):
            new_template[i] = template[template_keys[template_keys_idx]]
            i += 1
            template_keys_idx += 1
        else:
            if template_keys[template_keys_idx] < add_template_keys[add_template_keys_idx]:
                new_template[i] = template[template_keys[template_keys_idx]]
                i += 1
                template_keys_idx += 1
            else:
                new_template[i] = add_template[add_template_keys[add_template_keys_idx]]
                i += 1
                add_template_keys_idx += 1

    template = new_template

result = template.values()
c = dict(Counter(result))
maximum = 0
for i in c:
    if c[i] > maximum:
        maximum = c[i]

minimum = maximum
for i in c:
    if c[i] < minimum:
        minimum = c[i]
    
print(maximum - minimum)