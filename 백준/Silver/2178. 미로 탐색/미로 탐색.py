from collections import deque
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(N)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
q = deque()
q.append((0, 0))

def dfs():
    while q:
        x, y = q.popleft()
        for k in range(len(d)):
            dx = x + d[k][0]
            dy = y + d[k][1]
            if 0 <= dx < N and 0 <= dy < M:
                if maze[dx][dy] == 1:
                    maze[dx][dy] = maze[x][y] + 1
                    q.append((dx, dy))

dfs()
print(maze[N-1][M-1])