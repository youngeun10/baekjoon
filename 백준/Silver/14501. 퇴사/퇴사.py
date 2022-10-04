from sys import stdin

n = int(stdin.readline())
arr = [tuple(map(int, stdin.readline().rstrip().split())) for _ in range(n)]
dp = [0 for _ in range(n+1)]

for i in range(n-1, -1, -1):
    if i + arr[i][0] > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], arr[i][1] + dp[i + arr[i][0]])

print(dp[0])