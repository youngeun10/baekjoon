import sys
input = sys.stdin.readline

n = int(input())
numArr = list(map(int, input().split()))
dp = [0] * n
dp[0] = numArr[0]

for i in range(1, n):
    dp[i] = max(numArr[i], dp[i-1]+numArr[i])

print(max(dp))