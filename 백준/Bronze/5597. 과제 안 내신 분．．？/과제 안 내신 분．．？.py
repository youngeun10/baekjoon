import sys
input = sys.stdin.readline

result = []
numArr = [int(input().rstrip()) for i in range(28)]

for i in range(1, 31):
    if i not in numArr:
        result.append(i)

print(*result, sep="\n")