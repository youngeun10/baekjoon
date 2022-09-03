from sys import stdin

n = int(stdin.readline())
arr = {}
for _ in range(n):
    i = int(stdin.readline())
    if i in arr:
        arr[i] += 1
    else:
        arr[i] = 1
tmp = sorted(arr.items())
result = sorted(dict(tmp).items(), key=lambda x: x[1], reverse=True)
print(result[0][0])