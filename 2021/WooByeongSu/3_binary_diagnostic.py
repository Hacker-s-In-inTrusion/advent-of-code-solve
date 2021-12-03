lines = None
with open("./input.txt", "r") as f:
    lines = f.readlines()

# part 1
bits = [line[:-1] for line in lines]
num_of_bits = len(bits)
num_of_one_line_bits = len(bits[0])
half_of_num_of_bits = num_of_bits / 2
gamma = 0
for i in range(num_of_one_line_bits):
    temp = 0
    for j in range(num_of_bits):
        if bits[j][i] == '1':
            temp += 1
        if temp > half_of_num_of_bits:
            gamma += 2 ** (num_of_one_line_bits - i - 1)
            break

epsilon = 2 ** num_of_one_line_bits - 1 - gamma
print(gamma * epsilon)

# part 2
O2_answer = bits
for i in range(num_of_one_line_bits):
    if len(O2_answer) == 1:
        break
    count = 0
    dominant = '1'
    half_of_O2_answer_len = len(O2_answer) / 2
    for bit in O2_answer:
        if bit[i] == '0':
            count += 1
        if count > half_of_O2_answer_len:
            dominant = '0'
            break
    O2_answer = [a for a in O2_answer if a[i] == dominant]

CO2_answer = bits
for i in range(num_of_one_line_bits):
    if len(CO2_answer) == 1:
        break
    count = 0
    dominant = '1'
    half_of_CO2_answer_len = len(CO2_answer) / 2
    for bit in CO2_answer:
        if bit[i] == '0':
            count += 1
        if count > half_of_CO2_answer_len:
            dominant = '0'
            break
    CO2_answer = [a for a in CO2_answer if a[i] != dominant]

print(int(O2_answer[0], 2) * int(CO2_answer[0], 2))