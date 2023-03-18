import sys
from collections import deque
input = sys.stdin.readline

q = deque([i for i in range(1, int(input())+1)])

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())
print(q[0])