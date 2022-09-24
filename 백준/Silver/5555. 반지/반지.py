from sys import stdin
from collections import deque

w = stdin.readline().rstrip()
cnt = 0

for _ in range(int(stdin.readline())):
    r = stdin.readline().rstrip()
    if w in r:
        cnt += 1
    else:
        ring = list(r)
        word = list(w)
        chk = [i for i in range(len(ring)) if ring[i] == word[0]]
        for i in chk:
            ringd = deque(ring)
            ringd.rotate(-1 * i)
            result = ''.join(list(ringd))
            if w in result:
                cnt += 1
                break
print(cnt)