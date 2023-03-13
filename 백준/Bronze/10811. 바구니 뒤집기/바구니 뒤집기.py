import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = [i for i in range(1, n+1)]
numArr = [list(map(int, input().split())) for _ in range(m)]

for s, e in numArr:
    l = (e-s)//2 + 1 if (e-s)%2 == 1 else (e-s)//2
    s -= 1
    e -= 1
    for i in range(l):
        tmp = result[s+i]
        result[s+i] = result[e-i]
        result[e-i] = tmp
    
print(*result)