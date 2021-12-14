octopus = []

def add_one():
    for y in range(len(octopus)):
        for x in range(len(octopus[0])):
            octopus[y][x] += 1

with open("input.txt", "r") as f:
    while True:
        line = f.readline()
        if not line:
            break
        line = line[:-1]
        octopus.append([int(i) for i in line])

x_len = len(octopus[0])
y_len = len(octopus)

flash = 0
first_all_octopuses_flash = 0

i = 1
while True:
    add_one()
    flag = True
    is_flashed = [[False for _ in range(y_len)] for _ in range(x_len)]
    while True:
        for y in range(y_len):
            for x in range(x_len):
                if octopus[y][x] > 9:
                    if is_flashed[y][x]:
                        continue
                    for yy in range(y - 1, y + 2):
                        for xx in range(x - 1, x + 2):
                            if xx < 0 or xx >= x_len:
                                continue
                            if yy < 0 or yy >= y_len:
                                continue
                            if xx == x and yy == y:
                                continue
                            octopus[yy][xx] += 1
                    is_flashed[y][x] = True
                    flag = False
        if not flag:
            flag = True
        else:
            break
    
    for y in range(y_len):
        for x in range(x_len):
            if octopus[y][x] > 9:
                octopus[y][x] = 0
                if i < 101:
                    flash += 1
    
    flag = True

    for y in range(y_len):
        for x in range(x_len):
            if octopus[y][x] != 0:
                flag = False
                break
        if not flag:
            break

    if flag and first_all_octopuses_flash == 0:
        first_all_octopuses_flash = i
    
    if i > 100 and first_all_octopuses_flash != 0:
        break
    i += 1

print(flash)
print(first_all_octopuses_flash)