import sys
input = sys.stdin.readline

numArr = [list(map(int, input().split())) for _ in range(5)]
result = [0, 0]

for i in range(5):
    if result[1] < sum(numArr[i]):
        result = [i+1, sum(numArr[i])]
print(*result)