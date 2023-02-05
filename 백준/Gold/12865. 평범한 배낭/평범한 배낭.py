from sys import stdin

N, K = map(int, stdin.readline().rstrip().split())
dp = [0] * (K+1)
for _ in range(N):
    tmp = dp[:]
    w, v = map(int, stdin.readline().rstrip().split())
    for i in range(w, K+1):
        tmp[i] = max(dp[i-w]+v, dp[i])
    dp = tmp[:]
print(dp[K])