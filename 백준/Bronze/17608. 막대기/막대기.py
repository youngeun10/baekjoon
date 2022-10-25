from sys import stdin

n = int(stdin.readline())
arr = [int(stdin.readline()) for _ in range(n)]
tmp = arr[-1]
cnt = 1

for i in range(n-2, -1, -1):
    if arr[i] > tmp:
        cnt += 1
        tmp = arr[i]

print(cnt)