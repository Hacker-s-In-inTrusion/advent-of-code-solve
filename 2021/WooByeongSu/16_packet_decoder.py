import math

value = None
with open('input.txt', 'r') as f:
    value = f.readline()[:-1]

n = int(value, 16)
binary = ''
for _ in range(len(value) * 4):
    binary = str(n % 2) + binary
    n = n >> 1


i = 0
part1 = 0
def parse(packet, idx):
    global part1
    value = None
    if idx >= len(packet):
        return value, idx
    version = int(packet[idx:idx + 3], 2)
    part1 += version
    idx += 3
    typeID = int(packet[idx:idx + 3], 2)
    idx += 3
    if typeID == 4:
        temp = ""
        while True:
            is_last = (int(packet[idx]) == 0)
            idx += 1
            temp += packet[idx:idx+4]
            idx += 4
            if is_last:
                value = int(temp, 2)
                return value, idx
    else:
        length_type_id = int(packet[idx])
        idx += 1
        temp = []
        if length_type_id == 0:
            length = int(packet[idx:idx+15], 2)
            idx += 15
            end = idx + length
            while idx < end:
                tmp, idx = parse(packet, idx)
                temp.append(tmp)
        else:
            number = int(packet[idx:idx+11], 2)
            idx += 11
            for _ in range(number):
                tmp, idx = parse(packet, idx)
                temp.append(tmp)
        if typeID == 0:
            value = sum(temp)
        elif typeID == 1:
            value = math.prod(temp)
        elif typeID == 2:
            value = min(temp)
        elif typeID == 3:
            value = max(temp)
        elif typeID == 5:
            value = 1 if temp[0] > temp[1] else 0
        elif typeID == 6:
            value = 1 if temp[0] < temp[1] else 0
        elif typeID == 7:
            value = 1 if temp[0] == temp[1] else 0

    return value, idx

part2, _ = parse(binary, 0)
print(part1)
print(part2)