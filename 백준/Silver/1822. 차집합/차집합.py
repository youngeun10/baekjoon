from sys import stdin
n, m = map(int, stdin.readline().rstrip().split())
setA = set(map(int, stdin.readline().rstrip().split()))
setB = set(map(int, stdin.readline().rstrip().split()))
result = sorted(setA-setB)
print(len(result))
print(*result)