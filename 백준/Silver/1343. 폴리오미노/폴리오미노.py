def polyomino(s, a, b):
    while True:
        if s.find(a) >= 0:
            s = s.replace(a, b)
        else:
            break
    return s

from sys import stdin
board = stdin.readline().rstrip()

board = polyomino(board, 'XXXX', 'AAAA')
board = polyomino(board, 'XX', 'BB')

if board.find('X') >= 0:
    print(-1)
else:
    print(board)