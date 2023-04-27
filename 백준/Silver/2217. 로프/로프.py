import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
result = [0] * n

for i in range(n):
    result[i] = arr[i] * (n - i)

print(max(result))