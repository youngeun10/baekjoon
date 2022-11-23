from sys import stdin

n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split())) + [0]
cnt = 0
l, r = 0, 1
s = arr[l]

while r < len(arr):
    if s < m:
        s += arr[r]
        r += 1
    elif s == m:
        cnt += 1
        l += 1
        s = arr[l]
        r = l + 1
    else:
        l += 1
        s = arr[l]
        r = l + 1

print(cnt)
