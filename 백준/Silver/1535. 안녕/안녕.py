from sys import stdin

n = int(stdin.readline())
st = [0] + list(map(int, stdin.readline().rstrip().split()))       # 체력
joy = [0] + list(map(int, stdin.readline().rstrip().split()))       # 기쁨
dp = [[0] * 101 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, 101):
        if st[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-st[i]] + joy[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][99])