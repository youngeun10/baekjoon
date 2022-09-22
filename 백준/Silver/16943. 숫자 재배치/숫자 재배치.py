from sys import stdin
from itertools import permutations

a, b = stdin.readline().rstrip().split()
b = int(b)
a_arr = []
c = -1

for i in permutations(a):
    a_arr.append(''.join(i))

for i in a_arr:
    if i[0] == '0':
        continue
    i = int(i)
    if i < b:
        c = max(c, i)

print(c)