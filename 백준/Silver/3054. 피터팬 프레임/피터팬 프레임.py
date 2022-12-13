from sys import stdin
from collections import deque

s = deque(list(stdin.readline().rstrip()))
n = (len(s)*4) + 1
arr = [['.'] * n for _ in range(5)]
sign = '#'

for i in range(n):
    if i % 12 == 8 and n-i >= 5:
        sign = '*'
    elif i % 12 == 1:
        sign = '#'

    if i % 4 == 2:
        arr[0][i] = sign
        arr[4][i] = sign
        arr[2][i] = s.popleft()
    elif i % 2 == 1:
        arr[1][i] = sign
        arr[3][i] = sign
    elif i % 4 == 0:
        arr[2][i] = sign


for i in arr:
    print(*i, sep='')