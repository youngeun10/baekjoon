from sys import stdin
board = stdin.readline().rstrip()

board = board.replace('XXXX', 'AAAA')
board = board.replace('XX', 'BB')

print(-1) if 'X' in board else print(board)