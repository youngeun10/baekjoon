from sys import stdin

n = int(stdin.readline())
arr = [int(stdin.readline()) for _ in range(n)]
tmp = 0

for i in range(len(arr)):
    if i % 2 == 0:
        tmp += arr[i]
    else:
        tmp -= arr[i]

tmp = tmp // 2

for i in range(len(arr)):
    print(tmp)
    tmp = arr[i] - tmp