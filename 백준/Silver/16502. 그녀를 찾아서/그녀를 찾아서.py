from sys import stdin

d = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
tmp = {0: [], 1: [], 2: [], 3: []}
result = [0] * 4

t = int(stdin.readline())
rt = int(stdin.readline())

for i in range(rt):
    s, e, v = stdin.readline().split()
    tmp[d[s]].append((d[e], float(v)))

def dfs(cnt, time, cur):    # cnt : cnt, time : 현재까지의 시간 합, cur : 현재 노드
    if cnt == t:
        result[cur] += (time*100)
        return
    for i, j in tmp[cur]:
        dfs(cnt+1, time*j, i)

for i in range(4):
    dfs(0, 1, i)

for i in range(4):
    print(format(result[i]/4, '.2f'))