from collections import deque

N = int(input())
dq = deque()

dq.appendleft(N)

for n in range(N - 1, 0, -1):
    dq.appendleft(n)

    for j in range(n):
        moveCard = dq.pop()
        dq.appendleft(moveCard)

print(*dq)