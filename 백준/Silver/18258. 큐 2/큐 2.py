import sys
from collections import deque
input = sys.stdin.readline
q = deque([])

for _ in range(int(input())):
    tmp = input().split()

    if tmp[0] == "push":
        q.append(tmp[1])
    elif tmp[0] == "pop":
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif tmp[0] == "size":
        print(len(q))
    elif tmp[0] == "empty":
        print(1) if len(q) == 0 else print(0)
    elif tmp[0] == "front":
        print(-1) if len(q) == 0 else print(q[0])
    elif tmp[0] == "back":
        print(-1) if len(q) == 0 else print(q[-1])