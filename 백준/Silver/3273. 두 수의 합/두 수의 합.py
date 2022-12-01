from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
x = int(stdin.readline())

arr.sort()

if n <= 2:
    print(1) if n == 2 and sum(arr) == x else print(0)
    exit()

i, j = 0, n-1
cnt = 0

while True:
    if i >= j:
        break

    if arr[i] + arr[j] == x:
        i += 1
        j -= 1
        cnt += 1
    elif arr[i] + arr[j] > x:
        j -= 1
    else:
        i += 1
        j = n-1

print(cnt)