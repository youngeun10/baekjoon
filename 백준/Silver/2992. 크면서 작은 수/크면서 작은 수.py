from itertools import permutations
from sys import stdin

n = list(stdin.readline().rstrip())
arr = list(permutations(n, len(n)))
arr = sorted(set(arr))
idx = arr.index(tuple(n))
print(0 if tuple(n) == arr[-1] else ''.join(arr[idx+1]))