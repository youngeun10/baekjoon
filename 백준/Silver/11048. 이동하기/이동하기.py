from sys import stdin

n, m = map(int, stdin.readline().split())
dp = [list(map(int, stdin.readline().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            continue
        if i == 0:
            dp[i][j] = dp[i][j] + dp[i][j-1]
            continue
        if j == 0:
            dp[i][j] = dp[i][j] + dp[i-1][j]
            continue

        dp[i][j] = dp[i][j] + max(dp[i-1][j], dp[i][j-1])

print(dp[n-1][m-1])