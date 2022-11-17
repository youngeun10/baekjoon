from sys import stdin

n = int(stdin.readline())
m = 0
arr = []

for _ in range(n):
    a, b = map(int, stdin.readline().split())
    m = max(a, b, m)
    arr.append([a, b])

dp = [[0] * (m+1) for _ in range(m+1)]

for i in range(1, m+1):
    for j in range(1, i+1):
        if j == 1:
            dp[i][j] = i
        elif i == j:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

for a, b in arr:
    if a > b:
        print(dp[a][b])
    else:
        print(dp[b][a])