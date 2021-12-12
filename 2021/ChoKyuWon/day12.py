from os import path
from aocd.models import Puzzle
from collections import deque
import networkx

p = Puzzle(2021, 12)
input_str = p.input_data
# input_str="""fs-end
# he-DX
# fs-he
# start-DX
# pj-DX
# end-zg
# zg-sl
# zg-pj
# pj-he
# RW-he
# fs-DX
# pj-RW
# zg-RW
# start-pj
# he-WI
# zg-he
# pj-fs
# start-RW"""

data = input_str.split("\n")

nodes = []
for e in data:
    for v in e.split("-"):
        if v not in nodes:
            nodes.append(v)

g = {}
for node in nodes:
    g[node] = []

for e in data:
    n1 = e.split("-")[0]
    n2 = e.split("-")[1]
    g[n1].append(n2)
    g[n2].append(n1)

history = []
count = 0

pathlist = []
def p1_dfs(node, graph, path):
    if node == "end":
        pathlist.append(path)
        return
    if node.islower():
        path.append(node)
    for v in graph[node]:
        if v not in path:
            p1_dfs(v, graph, path.copy())


pathlist = []
def p2_dfs(node, graph, arg):
    flag = arg[0]
    path = arg[1]
    path.append(node)
    for v in graph[node]:
        if v == "start":
            continue
        if node == "end":
            pathlist.append(path)
            return
        if v.islower():
            if v not in path:
                p2_dfs(v,graph, (flag, path.copy()))
            elif (flag == False) and (path.count(v) == 1) :
                p2_dfs(v, graph, (True, path.copy()))
        else: p2_dfs(v, graph, (flag, path.copy()))
p2_dfs("start", g, (False, []))
print(len(pathlist))