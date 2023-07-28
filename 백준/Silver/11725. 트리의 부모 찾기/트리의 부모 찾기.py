from collections import deque
from sys import stdin

def bfs(graph, s, visited):
    queue = deque([s])
    visited[s] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                result[i] = v
                queue.append(i)
                visited[i] = True

input = stdin.readline
N = int(input())
graph, result = {}, {}
visited = [False] * (N+1)

for i in range(1, N+1):
    result[i] = 0
    graph[i] = []

for _ in range(1, N):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

bfs(graph, 1, visited)

for i in range(2, N+1):
    print(result[i])