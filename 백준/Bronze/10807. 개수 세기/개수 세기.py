from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
chk = int(stdin.readline())
d = {}

for i in arr:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d[chk]) if chk in d else print(0)