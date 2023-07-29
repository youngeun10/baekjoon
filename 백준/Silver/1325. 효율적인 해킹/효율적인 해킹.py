from sys import stdin
from collections import deque


N, M = map(int, stdin.readline().split())
result = [0] * (N+1)                        # 최장 경로 저장
comLinked = [ [] for _  in range(N+1)]      # 연결 정보 저장

for _ in range(M):
    a, b = map(int, stdin.readline().split())
    comLinked[b].append(a)


def bfs(s):
    q = deque([s])

    visited = [0] * (N+1)
    visited[s] = 1

    while q:
        v = q.popleft()
        for c in comLinked[v]:
            if not visited[c]:
                q.append(c)
                visited[c] = 1

    return sum(visited)

maxValue = 0
result = []
for i in range(1, N+1):
    tmp = bfs(i)
    if maxValue < tmp:
        result.clear()
        result.append(i)
        maxValue = tmp
    elif maxValue == tmp:
        result.append(i)

print(*result)