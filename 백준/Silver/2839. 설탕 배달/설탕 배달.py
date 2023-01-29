from sys import stdin

# 3키로, 5키로 봉지가 있음.
n = int(stdin.readline())
r = (n//5) + 1
c = (n//3) + 1
result = 10**9

dp = [[0] * r for _ in range(c)]

for i in range(r):
    for j in range(c):
        if (i*5) + (j*3) == n:
            result = min(i+j, result)

print(-1) if result == 10**9 else print(result)