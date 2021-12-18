from aocd.models import Puzzle
from math import floor, ceil
# p = Puzzle(2021, 18)
# input_str = p.input_data
input_str = """[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]"""

data = input_str.split("\n")

def split_pair(s:str):
    stack = 0
    index = 0
    for i, ch in enumerate(s):
        if ch == "[":
            stack += 1
        elif ch == "]":
            stack -= 1
        elif ch == "," and stack == 1:
            index = i
    return (s[1:index], s[index + 1:-1])

class Graph():
    def __init__(self, s:str, height:int, parent=None, sub_left=None, sub_right=None):
        if (sub_left != None) and (sub_left!= None):
            self.left = sub_left
            self.left.parent = self
            self.right = sub_right
            self.right.parent = self
            self.h = 0
            return
        self.parent = parent
        self.h = height
        left, right = split_pair(s)
        if len(left) == 1: self.left = int(left)
        else: self.left = Graph(left, height + 1, self)
        if len(right) == 1: self.right = int(right)
        else:self.right = Graph(right, height + 1, self)
    
    def magnitute(self):
        if isinstance(self.left, int): left = self.left
        else: left = self.left.magnitute()
        
        if isinstance(self.right, int): right = self.right
        else: right = self.right.magnitute()

        return left*3 + right*2
    
    def isPair(self):
        if isinstance(self.left, int) and isinstance(self.right, int): return True
        else: return False
    def explode(self):
        target = self
        while target.isPair():
            target = target.left
        print("Find target!", target.left, target.right)
        exit()
        p = self.parent
        pos = self
        while pos is p.left:
            pos = pos.parent
            p = pos.parent

        
        p = self.parent
        pos = self
        if self.parent.left is self:
            pass
        else:
            pass
    
    def trim(self):
        if self.h >= 4:
            self.explode()
        
        if isinstance(self.left, int) == False:
            self.left = self.left.trim()
        else:
            if self.left > 10:
                self.left = Graph("[{},{}]".format(floor(self.left/2), ceil(self.left/2)), self.h +1, self)
        
        if isinstance(self.right, int) == False:
            self.right = self.right.trim()
        else:
            if self.right > 10:
                self.right = Graph("[{},{}]".format(floor(self.right/2), ceil(self.right/2)), self.h +1, self)
        
        return self

    def __add__(self, g):
        new_graph = Graph(None, None, None, self, g)
        new_graph.trim()
        return new_graph
    def __str__(self):
        s = "["
        s += str(self.left)
        s += ","
        s += str(self.right)
        s += "]"
        return s


g = Graph("[[[[4,3],4],4],[7,[[8,4],9]]]", 0)
g2 = Graph("[1,1]", 0)
g3 = g + g2
exit()
for i in range(1, len(data)):
    tmp = Graph(data[i], 0)
    g = g + tmp