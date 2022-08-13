from itertools import permutations
from sys import stdin

n = int(stdin.readline())
k = int(stdin.readline())
card = [stdin.readline().rstrip() for _ in range(n)]
tmp = []
tmp = tmp + list(permutations(card, k))
tmp = set(tmp)
result = [''.join(i) for i in tmp]
result = set(result)
print(len(result))