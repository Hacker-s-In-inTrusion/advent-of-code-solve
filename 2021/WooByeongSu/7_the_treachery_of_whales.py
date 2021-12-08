import numpy as np

num = None

with open('input.txt', 'r') as f:
    num = [int(n) for n in f.readline().split(",")]

# step 1

np_arr = np.array(num)
mid = np.median(np_arr)

diff = [abs(i - mid) for i in num]
print(sum(diff))

# step 2

start = min(num)
end = max(num)

val = []

g = lambda x: x * (x + 1) / 2
for i in range(start, end + 1):
    diff = [g(abs(a - i)) for a in num]
    val.append(sum(diff))

print(min(val))