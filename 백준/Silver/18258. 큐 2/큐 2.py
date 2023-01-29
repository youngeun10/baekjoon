from sys import stdin, stdout
from collections import deque

n = int(stdin.readline())
q = deque(list())
result = []

for _ in range(n):
    tmp = list(map(str, stdin.readline().split()))

    if tmp[0] == "push":
        q.append(tmp[1])
    elif tmp[0] == "front":
        result.append(q[0]) if len(q) != 0 else result.append(str(-1))
    elif tmp[0] == "back":
        result.append(q[-1]) if len(q) != 0 else result.append(str(-1))
    elif tmp[0] == "size":
        result.append(str(len(q)))
    elif tmp[0] == "empty":
        result.append(str(1)) if len(q) == 0 else result.append(str(0))
    else:
        if len(q) == 0:
            result.append(str(-1))
        else:
            result.append(str(q[0]))
            q.popleft()

print('\n'.join(result))