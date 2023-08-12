# 최초, 최대 2
import sys
input = sys.stdin.readline

T = int(input())
result = []
for _ in range(T):
    N = int(input())
    tmpArr = list(map(int, input().split()))
    result.append((min(tmpArr), max(tmpArr)))

for i in range(T):
    print(result[i][0], result[i][1])
