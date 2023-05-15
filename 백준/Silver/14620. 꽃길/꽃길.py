def dfs(c, s):
    global answer
    if c == 3:
        answer = min(answer, s)
        return

    for i in range(1, n-1):
        for j in range(1, n-1):
            if flowerSearch(i, j):
                for px, py in zip(dx, dy):
                    visited[i+px][j+py] = 1
                    s += ground[i+px][j+py]
                
                dfs(c+1, s)

                for px, py in zip(dx, dy):
                    visited[i + px][j + py] = 0
                    s -= ground[i + px][j + py]


def flowerSearch(x, y):
    for px, py in zip(dx, dy):
        if visited[x+px][y+py] == 1:
            return False
    return True


import sys
input = sys.stdin.readline

n = int(input())
ground = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 0, 0, 1]
dy = [0, -1, 0, 1, 0]
visited = [[0] * n for _ in range(n)]
answer = 10 ** 9

dfs(0, 0)
print(answer)