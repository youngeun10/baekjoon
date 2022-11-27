from sys import stdin

m, n = map(int, stdin.readline().split())
k = int(stdin.readline())

if k > m * n:
    print(0)
    exit()

board = [[0] * m for _ in range(n)]
board[0][0] = 1
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
c = 0
x, y = (0, 0)
for i in range(2, k+1):
    while True:
        a, b = move[c]
        dx = x + a
        dy = y + b

        if 0 <= dx < n and 0 <= dy < m and board[dx][dy] == 0:
            board[dx][dy] = i
            x = dx
            y = dy
            break
        else:
            c = (c+1) % 4
print(y+1, x+1)