with open('input.txt', 'r') as f:
    num = [int(n) for n in f.readline().split(",")]

status = {}
for i in range(0, 9):
    status[i] = num.count(i)

for _ in range(256):
    temp = status[0]
    for i in range(0, 8):
        status[i] = status[i + 1]
    status[8] = temp
    status[6] += temp

result = 0
for i in range(0, 9):
    result += status[i]

print(result)