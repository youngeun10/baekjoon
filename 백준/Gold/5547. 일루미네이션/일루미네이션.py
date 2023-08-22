import sys
yin = sys.stdin.readline

from collections import deque

def bfs(r, c):
    queue = deque([(r, c)])
    visited = [[False] * (R + 2) for _ in range(C + 2)]
    visited[r][c] = True
    cnt = 0

    while queue:
        _x, _y = queue.popleft()
        # _x 값이 홀 짝일 떄 다르게
        d = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (0, 1)] if _x % 2 == 0 else [(0, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
        for dx, dy in d:
            x = _x + dx
            y = _y + dy
            if 0 <= x < C + 2 and 0 <= y < R + 2:
                if arr[x][y] == 0 and not visited[x][y]:
                    queue.append((x, y))
                    visited[x][y] = True
                elif arr[x][y]:
                    cnt += 1
    return cnt

R, C = map(int, yin().split())
arr = [[0] * (R + 2) for _ in range(C+2)]
for i in range(1, C+1):
    arr[i][1:R-1] = map(int, yin().rstrip().split())

print(bfs(0, 0))