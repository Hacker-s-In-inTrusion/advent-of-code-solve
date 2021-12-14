import copy

links = []
starts = []
paths = []

with open('input.txt', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        temp = line[:-1].split("-")
        if 'start' in temp:
            starts.append(temp)
        else:
            links.append(temp)


def get_next_cave(cur, link):
    if link[0] == cur:
        return link[1]
    else:
        return link[0]

def dfs(history, twice_flag):
    cur = history[-1]

    if cur == 'end':
        paths.append(copy.deepcopy(history))
        return
        
    nexts = []
    for link in links:
        if cur in link:
            nexts.append(get_next_cave(cur, link))
    for next in nexts:
        '''
        # part 1
        if next.islower() and next in history:
            continue
        history.append(next)
        dfs(history, False)
        history.pop()
        '''
        # part 2
        if twice_flag:
            if next.islower() and next in history:
                continue
            history.append(next)
            dfs(history, True)
            history.pop()
        else:
            if next.islower() and next in history:
                history.append(next)
                dfs(history, True)
                history.pop()
            else:
                history.append(next)
                dfs(history, False)
                history.pop()


for start in starts:
    next = get_next_cave('start', start)
    history = ['start', next]
    dfs(history, False)

print(len(paths))