from sys import stdin

n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().split()))
tmp = [0] * n
c = 1
v = 0

while v != n:
    if arr.count(c):
        tmp[arr.index(c)] = v
        arr[arr.index(c)] = 0
        v += 1
    else:
        c += 1

print(*tmp)