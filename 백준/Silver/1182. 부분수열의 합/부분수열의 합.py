from sys import stdin


def back(idx):
    if len(tmp) > 0 and sum(tmp) == s:
        result.append(1)

    for i in range(idx, n):
        tmp.append(arr[i])
        back(i+1)
        tmp.pop()


n, s = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
tmp = []
result = []

back(0)

print(sum(result))