'''
count
a: 8
b: 6
c: 8
d: 7
e: 4
f: 9
g: 7

0: abcefg   42
1: cf       17
2: acdeg    34
3: acdfg    39
4: bcdf     30
5: abdfg    37
6: abdefg   41
7: acf      25
8: abcdefg  49
9: abcdfg   45
'''

part1 = 0
part2 = 0
with open('input.txt', 'r') as f:
    while True:
        temp = f.readline().split()
        if not temp:
            break
        word_count = {}
        digit = temp[:10]
        value = temp[11:]
        digit = ["".join(sorted(i)) for i in digit]
        value = ["".join(sorted(i)) for i in value]

        for i in digit:
            for j in i:
                if j not in word_count:
                    word_count[j] = 1
                else:
                    word_count[j] += 1

        for i in value:
            if len(i) == 2 or len(i) == 3 or len(i) == 4 or len(i) == 7:
                part1 += 1

        result = {}
        for i in digit:
            count_sum = 0
            for j in i:
                count_sum += word_count[j]
            if count_sum == 42:
                result[i] = 0
            elif count_sum == 17:
                result[i] = 1
            elif count_sum == 34:
                result[i] = 2
            elif count_sum == 39:
                result[i] = 3
            elif count_sum == 30:
                result[i] = 4
            elif count_sum == 37:
                result[i] = 5
            elif count_sum == 41:
                result[i] = 6
            elif count_sum == 25:
                result[i] = 7
            elif count_sum == 49:
                result[i] = 8
            elif count_sum == 45:
                result[i] = 9
        
        part2 += result[value[0]] * 1000 + result[value[1]] * 100 + result[value[2]] * 10 + result[value[3]]

print(part1)
print(part2)