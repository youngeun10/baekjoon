import sys
sys.setrecursionlimit(10**9)

def sheep(y, x):
    tmp[y][x] = '.'
    for dy, dx in d:
        yy, xx = y+dy, x+dx
        if (0 <= yy < h) and (0 <= xx < w) and tmp[yy][xx] == '#':
            sheep(yy, xx)


for _ in range(int(sys.stdin.readline())):
    h, w = map(int, sys.stdin.readline().split())
    tmp = [list(sys.stdin.readline().rstrip()) for _ in range(h)]
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if tmp[i][j] == '#':
                sheep(i, j)
                cnt += 1
    print(cnt)