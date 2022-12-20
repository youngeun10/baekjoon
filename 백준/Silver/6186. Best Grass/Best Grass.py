import sys
sys.setrecursionlimit(100000)
 
def dfs(y, x):
    graph[y][x] = '.'
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if ny >= 0 and nx >= 0 and ny < R and nx < C:
            if graph[ny][nx] == '#':
                dfs(ny, nx)
 
R,C = map(int, input().split())
graph = [list(sys.stdin.readline().strip()) for _ in range(R)]
count = 0
for i in range(R):
    for j in range(C):
        if graph[i][j] == '#':
            dfs(i, j)
            count += 1
 
print(count)