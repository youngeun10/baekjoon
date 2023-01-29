from sys import stdin
from collections import deque

n = int(stdin.readline())
q = deque(list())

for _ in range(n):
    tmp = list(map(str, stdin.readline().split()))

    if tmp[0] == "push":
        q.append(tmp[1])
    elif tmp[0] == "front":
        print(q[0]) if len(q) != 0 else print(-1) 
    elif tmp[0] == "back":
        print(q[-1]) if len(q) != 0 else print(-1)
    elif tmp[0] == "size":
        print(len(q))
    elif tmp[0] == "empty":
        print(1) if len(q) == 0 else print(0)
    else:
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
            q.popleft()