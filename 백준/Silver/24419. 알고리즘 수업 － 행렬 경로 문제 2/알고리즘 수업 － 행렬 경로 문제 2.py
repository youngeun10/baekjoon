from sys import stdin

n = int(stdin.readline())
m = [list(map(int, stdin.readline().split())) for _ in range(n)]
result = [[1]*n for _ in range(n)]

for i in range(1, n):
    result[i][0] = i + 1
    for j in range(1, n):
        result[i][j] = result[i-1][j] + result[i][j-1]

print((result[n-1][n-1]*2) % 1000000007, (n**2) % 1000000007)