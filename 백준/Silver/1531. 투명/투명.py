def chk(x1, y1, x2, y2):

    for i in range(x1-1, x2):
        for j in range(y1-1, y2):
            arr[(100*i) + j] += 1


from sys import stdin
from collections import Counter

n, m = map(int, stdin.readline().split())
arr = [0] * 10000

for _ in range(n):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    chk(x1, y1, x2, y2)

c = Counter(arr)
result = 0
for i in c.keys():
    if i > m:
        result += c[i]
print(result)