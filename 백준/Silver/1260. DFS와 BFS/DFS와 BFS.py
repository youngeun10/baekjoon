from sys import stdin
from collections import deque

def dfs(g, v, visited):

    if not visited[v]:
        result.append(v)
        visited[v] = True

    for i in g[v]:
        if not visited[i]:
            dfs(g, i, visited)


def bfs(g, s, visited):
    queue = deque([s])
    visited[s] = True

    while queue:
        v = queue.popleft()
        result.append(v)
        for i in g[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N, M, S = map(int, stdin.readline().split())
graph = {}
visited = [False] * (N+1)
result = []


for i in range(1, N+1):
    graph[i] = []

set = [list(map(int, stdin.readline().split())) for _ in range(M)]
set.sort(key=lambda x: (x[0] + x[1]))

for s, e in set:
    graph[s].append(e)
    graph[e].append(s)


dfs(graph, S, visited)
print(*result)
result = []
visited = [False] * (N+1)
bfs(graph, S, visited)
print(*result)
