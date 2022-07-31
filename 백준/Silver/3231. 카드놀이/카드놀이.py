import sys

n = int(sys.stdin.readline())
arr = list(enumerate([int(sys.stdin.readline().rstrip()) for i in range(n)]))
arr.sort(key=lambda x: x[1])
bft = arr[0][0]
cnt = 0

for i, j in arr:
    if bft > i:
        cnt += 1
    bft = i
print(cnt)