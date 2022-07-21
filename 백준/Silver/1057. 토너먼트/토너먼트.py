import sys
import math

n, j, h = map(int, sys.stdin.readline().split())
cnt = 1
s = 2

if j > n or h > n:
    print(-1)
    quit()

for _ in range(math.ceil(math.sqrt(n))+1):
    if (j-1) // s == (h-1) // s:
        print(cnt)
        quit()
    else:
        s *= 2
        cnt += 1
 