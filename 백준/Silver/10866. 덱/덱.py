from collections import deque
import sys

input = sys.stdin.readline

d = deque(list())
result = []
rear = -1

for _ in range(int(input())):
    tmp = list(map(str, input().split()))

    if tmp[0] == 'push_back':
        d.append(tmp[1])
        rear += 1
    elif tmp[0] == 'push_front':
        d.appendleft(tmp[1])
        rear += 1
    elif tmp[0] == 'pop_front':
        if rear >= 0:
            result.append(d.popleft())
            rear -= 1
        else:
            result.append(str(-1))
    elif tmp[0] == 'pop_back':
        if rear >= 0:
            result.append(d.pop())
            rear -= 1
        else:
            result.append(str(-1))
    elif tmp[0] == 'size':
        result.append(rear+1)
    elif tmp[0] == 'empty':
        result.append(1 if len(d) == 0 else str(0))
    elif tmp[0] == 'front':
        result.append(d[0] if rear >= 0 else str(-1))
    elif tmp[0] == 'back':
        result.append(d[rear] if rear >= 0 else str(-1))

print(*result, sep='\n')