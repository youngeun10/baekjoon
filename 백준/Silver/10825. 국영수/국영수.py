from sys import stdin

std = []

for _ in range(int(stdin.readline())):
    s, k, e, m = map(str, stdin.readline().split())
    std.append((s, int(k), int(e), int(m)))

std.sort(key= lambda x: (-x[1], x[2], -x[3], x[0]))

for i in std:
    print(i[0])