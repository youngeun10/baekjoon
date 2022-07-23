from sys import stdin
from collections import deque

n = int(stdin.readline())
arr = deque(list(map(int, stdin.readline().split())))
num = deque([i for i in range(1, n+1)])
result = []

for _ in range(n):
    result.append(num.popleft())
    n = arr.popleft()
    if n > 0:
        arr.rotate(-1 * (n-1))
        num.rotate(-1 * (n-1))
    else:
        arr.rotate(-1 * n)
        num.rotate(-1 * n)
print(*result)
