from collections import deque
import sys
input = sys.stdin.readline

# board
N = int(input())
board = [[0] * (N+1) for _ in range(N+1)]

# apple
K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    board[y][x] = 1

# Switching Direction
L = int(input())
switch = {}
for _ in range(L):
    t, d = map(str, input().split())
    switch[int(t)] = d

# direction x, y
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
direction = 0

x, y = 1, 1
board[x][y] = 2
snake = deque([[x, y]])

time = 1

while True:
    x, y = x + dx[direction], y + dy[direction]
    # 끝이 아니거나, 나를 밟지 않을 때
    if 0 < x <= N and 0 < y <= N and board[x][y] != 2:
        if board[x][y] != 1:
            delX, delY = snake.popleft()
            board[delX][delY] = 0
        snake.append([x, y])
        board[x][y] = 2
        if time in switch.keys():
            if switch[time] == 'L':
                direction = (direction - 1) % 4
            else:
                direction = (direction + 1) % 4
        time += 1
    else:
        print(time)
        break