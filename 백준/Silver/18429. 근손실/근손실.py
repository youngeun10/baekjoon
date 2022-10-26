from sys import stdin

n, k = map(int, stdin.readline().split())
tmp = stdin.readline().rstrip()
arr = [int(i) - k for i in tmp.split()]
result = []
visited = [False] * n


def back(d, money):
    if d == n:
        result.append(1)
        return
    for i in range(n):
        if visited[i] == False and money + arr[i] >= 500:
            visited[i] = True
            back(d + 1, money + arr[i])
            visited[i] = False


back(0, 500)
print(sum(result))