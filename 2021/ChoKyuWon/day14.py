from os import path
from aocd.models import Puzzle
from bs4 import element
p = Puzzle(2021, 14)
input_str = p.input_data
# input_str="""NNCB

# CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C"""

init_str = input_str.split("\n\n")[0]
rules_raw = input_str.split("\n\n")[1].split("\n")
rules = {}
for rule in rules_raw:
    tmp = rule.split("->")
    rules[tmp[0].strip()] = tmp[1].strip()

def p1_step(s:str)->str:
    ret = ""
    for index in range(len(s)):
        if s[index:index+2] in list(rules.keys()):
            ret += s[index]
            ret += rules[s[index:index+2]]
        else:
            ret += s[index]
    return ret

s = init_str
for _ in range(10):
    s = p1_step(s)

l = list(s)
elements = set(s)
counts = []
for elem in elements:
    counts.append(l.count(elem))
counts = sorted(counts)
print(counts[-1] - counts[0])


s = init_str
words = []
for index in range(len(s) - 1):
    words.append(s[index:index+2])

words_count = {}
for word in words:
    if word not in words_count.keys():
        words_count[word] = 1
    else:
        words_count[word] += 1


for i in range(40):
    new_dict = {}
    for key in words_count.keys():
        if key in rules.keys():
            new_words = [key[0] + rules[key], rules[key] + key[1]]
            for w in new_words:
                if w in new_dict.keys():
                    new_dict[w] += words_count[key]
                else: new_dict[w] = words_count[key]
    words_count = new_dict

alph_count = {}
for i in range(26):
    alph_count[chr(ord('A')+i)] = 0
for key in words_count.keys():
    alph_count[key[0]] += words_count[key]
alph_count[init_str[-1]] += 1

counts = []
for key in alph_count.keys():
    if alph_count[key] != 0 : counts.append(alph_count[key])

counts = sorted(counts)
print(counts[-1] - counts[0])