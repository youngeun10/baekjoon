from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
result = []

for i in arr:
    if i not in result:
        result.append(i)

result.sort()

print(*result)