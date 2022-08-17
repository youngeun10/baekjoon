def dfs(start):
    global cnt
    visited[start] = 1
    for i in store[start]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1

from sys import stdin
input = stdin.readline
n = int(input())
store = {}
for _ in range(int(input())):
    k, v = map(int, input().rstrip().split())
    if k not in store: store[k] = [v]
    else: store[k].append(v)
    if v not in store: store[v] = [k]
    else: store[v].append(k)

cnt = 0
visited = [0] * (n+1)

dfs(1)
print(cnt)