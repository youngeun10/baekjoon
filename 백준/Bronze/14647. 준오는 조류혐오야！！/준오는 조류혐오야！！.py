from sys import stdin

n, m = map(int, stdin.readline().split())
arr = [list(map(str, stdin.readline().split())) for _ in range(n)]
ninecnt = [[0] * m for _ in range(n)]

# 첫째줄: 행, 둘쨰줄: 열
for i in range(n):
    for j in range(m):
        ninecnt[i][j] = arr[i][j].count('9')

chk = [0] * (m+n)   #행, 열 9 카운트
for i in range(n):
    chk[i] = sum(ninecnt[i])
for j in range(n, (n + m)):
    for i in range(n):
        chk[j] += ninecnt[i][j-n]

print((sum(chk)//2) - max(chk))