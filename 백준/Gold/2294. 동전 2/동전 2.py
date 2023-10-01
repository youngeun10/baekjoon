import sys
yin = sys.stdin.readline

N, K = map(int, yin().split())      # 1 <= N <= 100, 1 <= K <= 100000
arr = [int(yin().rstrip()) for _ in range(N)]
dp = [10001] * (K+1)
dp[0] = 0

for a in arr:
    for i in range(a, K+1):
        dp[i] = min(dp[i], dp[i-a]+1)

print(dp[K]) if dp[K] != 10001 else print(-1)