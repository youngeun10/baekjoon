from sys import stdin
from collections import deque

n, c = map(int, stdin.readline().split())

d = deque([i for i in range(1, n+1)])
result = deque([])

for i in range(n):
    d.rotate(-1 * (c-1))
    result.append(d.popleft())

print('<', end='')
print(*result, sep=', ', end='')
print('>', end='')
