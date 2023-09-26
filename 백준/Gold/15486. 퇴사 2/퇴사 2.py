# Gold5 퇴사 2
import sys
yin = sys.stdin.readline

N = int(yin())
T, P = [0] * N, [0] * N

for i in range(N):
    t, p = map(int, yin().split())
    T[i] = t
    P[i] = p

dp = [0] * (N+1)
max_value = 0

for i in range(N-1, -1, -1):
    if i + T[i] <= N:
        dp[i] = max(max_value, P[i] + dp[i + T[i]])
        max_value = dp[i]
    else:
        dp[i] = max_value
print(max_value)