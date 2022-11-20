import sys
sys.setrecursionlimit(10**9)

d, c = map(int, sys.stdin.readline().split())
book = [tuple(map(int, sys.stdin.readline().split())) for _ in range(c)]
book.sort(key=lambda x: x[0])
visited = [False] * c
result = [0]


def back(idx, dcnt, pcnt):
    if result[-1] < pcnt:
        result.append(pcnt)

    for i in range(idx, c):
        if visited[i] == False and dcnt + book[i][0] <= d:
            visited[i] = True
            back(i+1, dcnt + book[i][0], pcnt + book[i][1])
            visited[i] = False

back(0, 0, 0)
print(result[-1])