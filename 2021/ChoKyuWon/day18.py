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
    def __init__(self, s:str, height:int, root=None, parent=None, sub_left=None, sub_right=None):
        if (sub_left != None) and (sub_left!= None):
            sub_left.parent = self
            sub_left.change_root(self)
            self.left = sub_left 

            sub_right.parent = self
            sub_right.change_root(self)
            self.right = sub_right

            self.h = -1
            self.inc_height()
            self.parent = None
            self.root = root
            return
        
        if root == None: self.root = self
        else: self.root = root
        self.parent = parent
        self.h = height
        left, right = split_pair(s)
        if len(left) == 1: self.left = int(left)
        else: self.left = Graph(left, height + 1, self.root, self)
        if len(right) == 1: self.right = int(right)
        else:self.right = Graph(right, height + 1, self.root, self)
    
    def split_node(self, left:bool):
        if left:
            val = self.left
            self.left = Graph("[{},{}]".format(floor(val/2), ceil(val/2)), self.h +1, self.root, self)
            print("After split:", str(self.root))
            if self.left.h >= 4:
                self.left.explode()
        else:
            val = self.right
            self.right = Graph("[{},{}]".format(floor(val/2), ceil(val/2)), self.h +1, self.root, self)
            print("After split:", str(self.root))
            if self.right.h >= 4:
                self.right.explode()
                
    def inc_height(self):
        self.h += 1
        if isinstance(self.left, int) == False: self.left.inc_height()
        if isinstance(self.right, int) == False: self.right.inc_height()
    
    def change_root(self, root):
        self.root = root
        if isinstance(self.left, int) == False: self.left.change_root(root)
        if isinstance(self.right, int) == False: self.right.change_root(root)

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
        lazy_split = []

        target = self
        while target.isPair() == False:
            target = target.left
        
        pos = target
        flag = False
        while True:
            if pos is pos.parent.right: break
            pos = pos.parent
            if pos.parent == None:
                flag = True
                break
        if flag == False:
            pos = pos.parent
            if isinstance(pos.left, int) == False:
                pos = pos.left
                while True:
                    if isinstance(pos.right, int): break
                    pos = pos.right
                pos.right += target.left
                if pos.right >= 10:
                    lazy_split.append((pos, False))
            else:
                pos.left += target.left
                if pos.left >= 10:
                    lazy_split.append((pos, True))

        pos = target
        flag = False
        while True:
            if pos is pos.parent.left: break
            pos = pos.parent
            if pos.parent == None:
                flag = True
                break
        if flag == False:
            pos = pos.parent
            if isinstance(pos.right, int) == False:
                pos = pos.right
                while True:
                    if isinstance(pos.left, int): break
                    pos = pos.left
                pos.left += target.right
                if pos.left >= 10:
                    lazy_split.append((pos, True))
            else:
                pos.right += target.right
                if pos.right >= 10:
                    lazy_split.append((pos, False))
        
        if target is target.parent.left: target.parent.left = 0
        else: target.parent.right = 0
        print("After explode:", str(self.root))
        for node, boolean in lazy_split:
            node.split_node(boolean)
    def trim(self):
        print("Before trim:", str(self.root))
        if self.h >= 4:
            print("explode:", str(self))
            self.explode()
        
        if isinstance(self.left, int) == False:
            self.left.trim()
        else:
            if self.left >= 10:
                print("split")
                self.split_node(True)
        
        if isinstance(self.right, int) == False:
            self.right.trim()
        else:
            if self.right >= 10:
                print("split")
                self.split_node(False)
        print("After trim:", str(self.root))


        

    def __add__(self, g):
        new_graph = Graph(None, None, None, None, self, g)
        new_graph.trim()
        return new_graph
    def __str__(self):
        s = "["
        s += str(self.left)
        s += ","
        s += str(self.right)
        s += "]"
        return s


g = Graph(data[0], 0)
for i in range(1, len(data)):
    tmp = Graph(data[i], 0)
    g = g + tmp

print(str(g))
