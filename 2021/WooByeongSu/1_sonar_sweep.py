lines = None
with open("./input.txt", "r") as f:
    lines = f.readlines()

values = [int(num[:-1]) for num in lines]

# step 1
cnt = 0
for i in range(1, len(values)):
    if values[i] > values[i - 1]:
        cnt += 1

print(cnt)


# step 2

window_values = [values[i] + values[i + 1] + values[i + 2] for i in range(len(values) - 2)]
cnt = 0
for i in range(1, len(window_values)):
    if window_values[i] > window_values[i - 1]:
        cnt += 1

print(cnt)
