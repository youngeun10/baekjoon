import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tmp = [list(map(int, input().split())) for _ in range(N)]
arr = [[0]*(N+1) for _ in range(N+1)]
arr[1][1] = tmp[0][0]

# 윤곽
for i in range(1, N+1):
    arr[1][i] = tmp[0][i-1] + arr[1][i-1]
    arr[i][1] = tmp[i-1][0] + arr[i-1][1]

for i in range(2, N+1):
    for j in range(2, N+1):
        arr[i][j] = arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1] + tmp[i-1][j-1]

result = []
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result.append(arr[x2][y2] - arr[x1-1][y2] - arr[x2][y1-1] + arr[x1-1][y1-1])

print(*result, sep='\n')