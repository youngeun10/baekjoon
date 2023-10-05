import sys
yin = sys.stdin.readline
from collections import deque

def bfs(s, m, e):
    visited = [0] * len(m)
    q = deque([s])
    s1, s2 = 0, 0

    while q:
        s1, s2 = q.popleft()
        for i in range(len(m)):
            if abs(s1 - e[0]) + abs(s2 - e[1]) <= 1000:
                return True

            if visited[i] or (abs(m[i][0] - s1) + abs(m[i][1] - s2)) > 1000:
                continue

            q.append(m[i])
            visited[i] = True

    return True if sum(visited) == len(m) and (abs(e[0] - s1) + abs(e[1] - s2)) <= 1000 else False

result = []
for _ in range(int(yin())):
    N = int(yin())
    house = tuple(map(int, yin().split()))
    store = list(tuple(map(int, yin().split())) for _ in range(N))
    rock = tuple(map(int, yin().split()))
    result.append("happy") if bfs(house, store, rock) else result.append("sad")

print(*result, sep="\n")