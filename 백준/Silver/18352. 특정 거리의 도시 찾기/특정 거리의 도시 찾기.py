def bfs(x):
    distance = [0] * (N+1)
    distance[x] = 0
    visited = [False] * (N+1)
    queue = deque([x])

    while queue:
        c = queue.popleft()
        visited[c] = True
        if c not in road:
            continue

        for i in road[c]:
            if distance[i] == 0 and not visited[i]:
                distance[i] = distance[c] + 1
                queue.append(i)
                
    return distance

import sys
from collections import deque

input = sys.stdin.readline

# N: 도시 수, M: 도로 수, K: 거리 정보, X: 출발 위치
N, M, K, X = map(int, input().split())
road = {}
for _ in range(M):
    s, e = map(int, input().split())
    if s not in road:
        road[s] = [e]
    else:
        road[s].append(e)

result = bfs(X)

if K in result:
    for i in range(len(result)):
        if result[i] == K:
            print(i)
else:
    print(-1)