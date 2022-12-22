from sys import stdin
from itertools import combinations

n, m, k = map(int, stdin.readline().split())
pick = combinations(range(1, n+1), m)

a_lis = []
lis = []
cnt = 0

for i in pick:
    i = [*i]
    a_lis.append(i)

b_lis = a_lis.copy()

for a in a_lis:
    for b in b_lis:
        lis.extend(a)
        lis.extend(b)
        pre_len = len(lis)
        lis = set(lis)
        aft_len = len(lis)
        lis = []

        if pre_len - aft_len >= k:
            cnt += 1

num = len(a_lis)
print(cnt/num**2)