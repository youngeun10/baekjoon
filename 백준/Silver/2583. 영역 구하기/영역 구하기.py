from collections import deque
from sys import stdin
input = stdin.readline

m, n, k = map(int, input().split())
board = [[0] * n for i in range(m)]

# 모눈종이 칠하기
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            board[i][j] = 1

# 모눈종이 전체를 탐색하며 BFS 진행
q = deque()
area = []
move = [(1, 0), (0, 1), (-1, 0),(0, -1)]
for i in range(m):
    for j in range(n):
        if not board[i][j]:
            board[i][j] = 1
            q.append((i, j))
            area.append(1)
            while(q):
                x, y = q.popleft()
                for a, b in move:
                    dx = x + a; dy = y+b
                    if m > dx >= 0 and n > dy >= 0 and not board[dx][dy]:
                        q.append((dx, dy))
                        board[dx][dy] = 1
                        area[-1] += 1
print(len(area))
print(*sorted(area))