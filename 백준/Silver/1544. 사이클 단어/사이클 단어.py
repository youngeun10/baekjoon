from sys import stdin
from collections import deque

store = []
cnt = 0
for _ in range(int(stdin.readline())):
    s = deque(stdin.readline().rstrip())

    if ''.join(i for i in s) not in store:
        cnt += 1
        for i in range(len(s)):
            s.rotate(-1)
            store.append(''.join(i for i in s))
print(cnt)