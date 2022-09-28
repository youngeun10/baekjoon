import sys
import math
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m,n,x,y = map(int,input().split())
    lcm = math.lcm(m,n)
    tf = False
    year = x

    maxMN = max(m, n)
    if maxMN == m:
        xy = (x,y)
    else:
        xy = (y,x)
    minMN = min(m, n)
    
    i = 0
    while True:
        year = xy[0] + i * maxMN

        if year > lcm:
            break
        
        if year % minMN == xy[1]:
            tf = True
            break

        if year % minMN == 0 and xy[1] == minMN:
            tf = True
            break

        i += 1
    if not tf:
        year = -1
    print(year)