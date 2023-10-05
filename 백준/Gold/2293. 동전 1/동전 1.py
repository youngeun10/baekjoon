from sys import stdin
yin = stdin.readline

N, K = map(int, yin().split())
arr = [int(yin().strip()) for _ in range(N)]
dp = [0] * (K+1)
dp[0] = 1

for i in arr:
    for n in range(i, K+1):
        dp[n] = dp[n] + dp[n-i]
print(dp[K])