from collections import deque
import sys
input = sys.stdin.readline

def directionChange(d, c):
    if c == 'L':
        return (d-1) % 4
    else:
        return (d+1) % 4

N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1
L = int(input())
times = {}
for i in range(L):
    X, C = input().split()
    times[int(X)] = C

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

direction = 1
time = 1
y, x = 0, 0
snake = deque([[y, x]])
board[y][x] = 2

while True:
    y, x = y + dy[direction], x + dx[direction]
    if 0 <= y < N and 0 <= x < N and board[y][x] != 2:
        if not board[y][x] == 1:
            delY, delX = snake.popleft()
            board[delY][delX] = 0
        board[y][x] = 2
        snake.append([y, x])
        if time in times.keys():
            direction = directionChange(direction, times[time])
        time += 1
    else:
        print(time)
        break