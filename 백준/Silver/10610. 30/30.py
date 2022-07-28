from sys import stdin

n = list(map(int, stdin.readline().strip()))
n.sort(reverse=True)

if n[-1] != 0 or sum(n) % 3 != 0:
    print(-1)
else:
    print(*n, sep='')