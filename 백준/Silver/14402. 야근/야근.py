from sys import stdin

p = int(stdin.readline())
tmp = {}
cnt = 0

for _ in range(p):
    n, s = map(str, stdin.readline().split())

    if s == '-':
        if n not in tmp or tmp[n] == 0:
            cnt += 1
        elif n in tmp:
            tmp[n] -= 1
    else:
        if n not in tmp:
            tmp[n] = 1
        else:
            tmp[n] += 1

print(cnt) if len(tmp) == 0 else print(sum(tmp.values()) + cnt)