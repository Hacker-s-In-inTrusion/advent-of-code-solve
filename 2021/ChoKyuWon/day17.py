from aocd.models import Puzzle
p = Puzzle(2021, 17)
input_str = p.input_data
# input_str = "target area: x=20..30, y=-10..-5"

class Area():
    def __init__(self, min_x, max_x, min_y, max_y):
        self.x = list(range(min_x, max_x + 1))
        self.y = list(range(min_y, max_y + 1))

class Velocity():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def step(self):
        self.y -= 1
        if self.x < 0: self.x += 1
        elif self.x > 0 : self.x -= 1

class Probe():
    def __init__(self, x,y):
        self.x = 0
        self.y = 0
        self.velocity = Velocity(x,y)
    def __init__(self, v):
        self.velocity = v
        self.x = 0
        self.y = 0
        self.max_height = 0
    def step(self):
        self.x += self.velocity.x
        self.y += self.velocity.y
        self.max_height = max(self.max_height, self.y)
        self.velocity.step()
    
    def init(self, x, y):
        self.x = 0
        self.y = 0
        self.velocity = Velocity(x,y)


s = input_str.split(":")[1].strip().split(",")
area = Area(int(s[0].split("=")[1].split("..")[0]), int(s[0].split("=")[1].split("..")[1]), int(s[1].split("=")[1].split("..")[0]), int(s[1].split("=")[1].split("..")[1]))


max_height = (1<<64) * -1
count = 0

possible_x = []
for init_x in range(1000):
    pos_x = 0
    dx = init_x
    for step in range(1000):
        if pos_x in area.x:
            possible_x.append(init_x)
            break
        pos_x += dx
        dx -= 1

p = Probe((0,0))
for i in possible_x:
    for j in range(-1000,1000):
        v = Velocity(i,j)
        if j > abs(min(area.y)):
            break
        while True:
            p.step()
            if p.x in area.x and p.y in area.y:
                max_height = max(max_height, p.max_height)
                count += 1
                break
            if (p.x > max(area.x) and p.velocity.x >= 0) or (p.x < min(area.x) and p.velocity.x <= 0):
                break
            if (p.y < min(area.y) and p.velocity.y < 0):
                break
print(max_height, count)