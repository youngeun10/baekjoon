from sys import stdin
from itertools import combinations
from collections import Counter

xyz = [stdin.readline().rstrip() for _ in range(3)]
n = int(stdin.readline().rstrip())
arr = []
result = []

for i in xyz:
    for j in list(combinations(i, n)):
        arr.append(''.join(j))

counter = Counter(arr)
for i in counter:
    if counter[i] > 1:
        result.append(i)

result.sort()
print(*result, sep='\n') if len(result) > 0 else print(-1)