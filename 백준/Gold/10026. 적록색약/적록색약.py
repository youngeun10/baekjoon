import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
grim = [list(input().rstrip()) for _ in range(N)]

def colorBlindness(g):      # 색맹일 경우
    result = []
    for i in range(N):
        tmp = []
        for j in range(N):
            tmp.append('X') if g[i][j] in ('R', 'G') else tmp.append(g[i][j])
        result.append(tmp)
    return result

def bfs(x, y):       # 영역 구하기
    way = [(1, 0), (-1, 0), (0, -1), (0 ,1)]
    c = grim[x][y]
    q = deque([(x, y)])
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        for dx, dy in way:
            if x + dx >= N or x + dx < 0 or y + dy >= N or y + dy < 0:
                continue

            if not visited[x+dx][y+dy] and c == grim[x+dx][y+dy]:
                q.append((x+dx, y+dy))
                visited[x+dx][y+dy] = True

visited = [[False] * N for _ in range(N)]
result1  = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            result1 += 1

visited = [[False] * N for _ in range(N)]
grim = colorBlindness(grim)
result2 = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            result2 += 1

print(result1, result2)