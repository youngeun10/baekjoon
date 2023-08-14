import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(x, y, cnt):
    graph[x][y] = 0
    for dx, dy in dir:
        _x, _y = x + dx, y + dy
        if (0 <= _x < N and 0 <= _y < N) and graph[_x][_y]:
            cnt = dfs(_x, _y, cnt+1)
    return cnt

cnt = []

for r in range(N):
    for c in range(N):
        if graph[r][c]:
            cnt.append(dfs(r, c, 1))

cnt.sort()
print(len(cnt))
print(*cnt, sep="\n")