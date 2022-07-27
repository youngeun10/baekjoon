from sys import stdin

n, m = map(int, stdin.readline().split())
j = int(stdin.readline())
tarr = [int(stdin.readline()) for _ in range(j)]

arr = [i for i in range(1, m+1)]
cnt = 0

for t in tarr:

    if t in arr:
        continue

    elif max(arr) < t:
        cnt += t - max(arr)
        arr = [i + (t - max(arr)) for i in arr]

    elif min(arr) > t:
        cnt += min(arr) - t
        arr = [i - (min(arr) - t) for i in arr]

print(cnt)