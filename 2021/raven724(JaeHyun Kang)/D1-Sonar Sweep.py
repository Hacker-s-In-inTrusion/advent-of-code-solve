# Use text input file, not pip package


input_file = open("input.txt", "r")  # Open input file
res = 0                                              # Answer
# Part 1
"""
previous = int(input_file.readline())

while True:
    current = input_file.readline()
    if current:
        current = int(current)
        if current > previous:
            res += 1
        previous = current
    else:
        break
"""
# Part 2
previous = []
for _ in range(3):
    previous.append(int(input_file.readline()))

while True:
    current = previous[1:]
    current_num = input_file.readline()
    if current_num:
        current.append(int(current_num))
        if sum(previous) < sum(current):
            res += 1
        previous = current
    else:
        break
print(res)
