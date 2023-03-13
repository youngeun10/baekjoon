import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = [0] * n
basket = [list(map(int, input().split())) for _ in range(m)]

for i, j, k in basket:
    for x in range(i-1, j):
        result[x] = k

print(*result)