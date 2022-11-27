from sys import stdin

n = int(stdin.readline())
arr = [int(stdin.readline()) for _ in range(n)]

arr.sort(reverse=True)
sum = 0

for i in range(n):
    if arr[i] - i < 0:
        continue
    sum += (arr[i] - i)

print(sum)