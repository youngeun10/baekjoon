from sys import stdin

n = int(stdin.readline())
tmp = list(map(int, stdin.readline().split()))
result = 0
s = tmp[0]

for i in range(1, n):
    if tmp[i] < s:
        s = tmp[i]
    result = max(result, tmp[i]-s)

print(result)
