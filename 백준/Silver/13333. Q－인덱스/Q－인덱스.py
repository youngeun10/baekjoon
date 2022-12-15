from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
arr.sort()
chkArr = [0] * (arr[-1]+1)

for i in arr:
    chkArr[i] += 1

for k in range(arr[-1]+1):
    if k <= sum(chkArr[k:]) and n-k <= sum(chkArr[:k+1]):
        print(k)
        exit()