def dfs(x, y, a):
    if len(a) == 6:
        if a not in result:
            result.append(a)
        return

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx > 4 or ny < 0 or ny > 4:
            continue
        else:
            dfs(nx, ny, a + arr[nx][ny])

from sys import stdin
arr = [stdin.readline().rstrip().split() for _ in range(5)]
result = []
for i in range(5):
    for j in range(5):
        dfs(i, j, arr[i][j])
print(len(result))