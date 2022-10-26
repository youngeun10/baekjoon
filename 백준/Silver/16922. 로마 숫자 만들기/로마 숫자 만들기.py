import sys

sys.setrecursionlimit(10**7)
n = int(sys.stdin.readline())
arr = [1, 5, 10, 50]
tmp = []
result = []

def back(d, idx):
    if len(tmp) == n:
        if sum(tmp) not in result:
            result.append(sum(tmp))
        return
    for i in range(idx, 4):
        tmp.append(arr[i])
        back(d+1, i)
        tmp.pop()
back(0, 0)
print(len(result))