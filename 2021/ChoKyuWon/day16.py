from aocd.models import Puzzle
p = Puzzle(2021, 16)
input_str = p.input_data
#  input_str="""9C0141080250320F1802104A08"""

def hex2bin(s):
    ret = bin(int(s,16))[2:]
    return '0'*(4 - len(ret)) + ret

binary_tape = ""
for ch in input_str:
    binary_tape += hex2bin(ch)

class Packet():
    def __init__(self, version, id):
        self.version = version
        self.id = id
        self.subpacket = []
    def add_subpacket(self, packet):
        self.subpacket.append(packet)
    def add_literal(self, literal):
        self.literal = literal

def decode(binary_tape:str)->tuple:
    p = Packet(int(binary_tape[0:3],2), int(binary_tape[3:6],2))
    index = 6
    if p.id == 4:
        value = ""
        while True:
            raw = binary_tape[index:index+5]
            value += raw[1:]
            index += 5
            if raw[0] == '0':
                break
        p.add_literal(int(value,2))
        return (p, binary_tape[index:])
    else:
        I = binary_tape[index]
        index += 1
        L = 0
        if I == '0':
            L = int(binary_tape[index :index  + 15],2)
            index += 15
            arg = binary_tape[index:index + L]
            while True:
                if arg == "":
                    break
                sub, arg = decode(arg)
                p.add_subpacket(sub)
            remain = binary_tape [index + L:]
        else:
            L = int(binary_tape[index:index + 11],2)
            index += 11
            remain = binary_tape[index:]
            for i in range(L):
                sub, remain = decode(remain)
                p.add_subpacket(sub)
    return (p, remain)

count = 0
index = 0
packet_list = []
remain = binary_tape
while True:
    p, remain = decode(remain)
    packet_list.append(p)
    if remain == "":
        break
    if int(remain, 2) == 0:
        break


def version_sum(p):
    s = p.version
    for packet in p.subpacket:
        s += version_sum(packet)
    return s

def packet_process(p:Packet):
    op_list = []
    for packet in p.subpacket:
        op_list.append(packet_process(packet))
    if p.id == 0:
        return sum(op_list)
    elif p.id == 1:
        ret = 1
        for op in op_list:
            ret *= op
        return ret
    elif p.id == 2:
        return min(op_list)
    elif p.id == 3:
        return max(op_list)
    elif p.id == 4:
        return p.literal
    elif p.id == 5:
        if op_list[0] > op_list[1]: return 1
        else: return 0
    elif p.id == 6:
        if op_list[0] < op_list[1]: return 1
        else: return 0
    elif p.id == 7:
        if op_list[0] == op_list[1]: return 1
        else: return 0

count2 = 0
for p in packet_list:
    count += version_sum(p)
    count2 += packet_process(p)

print(count)
print(count2)