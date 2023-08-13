from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited = [[False] * N for _ in range(N)]
result = []

for r in range(N):
    for c in range(N):
        cnt = 0
        if visited[r][c] or graph[r][c] == 0:
            continue
        cnt += 1
        visited[r][c] = True
        queue = deque([(r, c)])
        while queue:
            _r, _c = queue.popleft()
            for dr, dc in dir:
                x, y = _r+dr, _c+dc
                if not (0 <= x < N and 0 <= y <N) or visited[x][y] or not graph[x][y]:
                    continue
                cnt += 1
                queue.append((x, y))
                visited[x][y] = True
        result.append(cnt)

print(len(result))
print(*sorted(result), sep="\n")