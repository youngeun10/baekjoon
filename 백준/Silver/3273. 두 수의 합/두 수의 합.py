from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
x = int(stdin.readline())
h = set()
cnt = 0

for i in arr:
    if i in h:
        cnt += 1
    elif i <= x:
        h.add(x-i)
print(cnt)