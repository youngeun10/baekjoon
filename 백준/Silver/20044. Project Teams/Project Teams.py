from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
arr.sort()
result = 10**9

for i in range(n):
    result = min(result, arr[i]+arr[(n*2)-1-i])

print(result)