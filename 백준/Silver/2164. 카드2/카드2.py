from sys import stdin
from collections import deque

q = deque([i for i in range(1, int(stdin.readline())+1)])

while len(q) > 1:
    q.popleft()
    tmp = q.popleft()
    q.append(tmp)

print(q[0])