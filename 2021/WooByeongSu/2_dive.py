lines = None
with open("./input.txt", "r") as f:
    lines = f.readlines()

# part 1
result = {"forward": 0, "down": 0, "up": 0}

for line in lines:
    l = line.split()
    result[l[0]] += int(l[1])
print(result["forward"] * (result["down"] - result["up"]))

# part 2
aim = 0
depth = 0
for line in lines:
    l = line.split()
    if l[0] == "down":
        aim += int(l[1])
    elif l[0] == "up":
        aim -= int(l[1])
    else:
        depth += (aim * int(l[1]))

print(result["forward"] * depth)