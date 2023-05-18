import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

numSet = {}
for a in arr:
    if a not in numSet:
        numSet[a] = 0

s, e = 0, 0
result = 0
while e < N:
    if numSet[arr[e]] < K:
        numSet[arr[e]] += 1
        e += 1
    else:
        numSet[arr[s]] -= 1
        s += 1
    result = max(e-s, result)

print(result)