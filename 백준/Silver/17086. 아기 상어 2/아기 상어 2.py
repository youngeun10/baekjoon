import sys
from collections import deque
input = sys.stdin.readline

n, m = tuple(map(int, input().split()))
shark_list = [list(map(int, input().split())) for _ in range(n)]

q = deque()
for i in range(n):
    for j in range(m):
        if shark_list[i][j] == 1:
            q.append([i, j])

ans = 0
dx = [-1, -1, -1, 0, 1, 0, 1, 1]
dy = [-1, 0, 1, 1, 1, -1, 0, -1]

while q:
    x, y = q.popleft()
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if shark_list[nx][ny] == 0:
                q.append([nx, ny])
                shark_list[nx][ny] = shark_list[x][y] + 1
                ans = max(ans, shark_list[x][y] + 1)

print(ans-1)