from sys import stdin

n = int(stdin.readline())
mine = [stdin.readline().rstrip() for _ in range(n)]
game = [stdin.readline().rstrip() for _ in range(n)]
chk = 0

for i in range(n):
    for j in range(n):
        if mine[i][j] == '*' and game[i][j] == 'x':
            chk = 1

for i in range(n):
    line = ""
    for j in range(n):
        cnt = 0
        if chk == 1 and mine[i][j] == '*':
            line += '*'
            continue

        if game[i][j] == 'x':
            if i == 0 and j == 0:
                if n == 1: print(0); exit()
                if mine[i][j + 1] == '*': cnt += 1
                if mine[i + 1][j + 1] == '*': cnt += 1
                if mine[i + 1][j] == '*': cnt += 1
            elif i == 0 and j == (n-1):
                if mine[i][j - 1] == '*': cnt += 1
                if mine[i + 1][j - 1] == '*': cnt += 1
                if mine[i + 1][j] == '*': cnt += 1
            elif i == (n-1) and j == (n-1):
                if mine[i][j - 1] == '*': cnt += 1
                if mine[i - 1][j - 1] == '*': cnt += 1
                if mine[i - 1][j] == '*': cnt += 1
            elif i == (n-1) and j == 0:
                if mine[i - 1][j] == '*': cnt += 1
                if mine[i - 1][j + 1] == '*': cnt += 1
                if mine[i][j + 1] == '*': cnt += 1
            elif i == 0 and 0 < j < (n-1):
                if mine[i][j - 1] == '*': cnt += 1
                if mine[i + 1][j - 1] == '*': cnt += 1
                if mine[i + 1][j] == '*': cnt += 1
                if mine[i + 1][j + 1] == '*': cnt += 1
                if mine[i][j + 1] == '*': cnt += 1
            elif i == (n-1) and 0 < j < (n-1):
                if mine[i][j - 1] == '*': cnt += 1
                if mine[i - 1][j - 1] == '*': cnt += 1
                if mine[i - 1][j] == '*': cnt += 1
                if mine[i - 1][j + 1] == '*': cnt += 1
                if mine[i][j + 1] == '*': cnt += 1
            elif 0 < i < (n-1) and j == 0:
                if mine[i - 1][j] == '*': cnt += 1
                if mine[i - 1][j + 1] == '*': cnt += 1
                if mine[i][j + 1] == '*': cnt += 1
                if mine[i + 1][j + 1] == '*': cnt += 1
                if mine[i + 1][j] == '*': cnt += 1
            elif 0 < i < (n-1) and j == (n-1):
                if mine[i - 1][j] == '*': cnt += 1
                if mine[i - 1][j - 1] == '*': cnt += 1
                if mine[i][j - 1] == '*': cnt += 1
                if mine[i + 1][j - 1] == '*': cnt += 1
                if mine[i + 1][j] == '*': cnt += 1
            elif 0 < i < (n-1) and 0 < j < (n-1):
                if mine[i - 1][j - 1] == '*': cnt += 1
                if mine[i - 1][j] == '*': cnt += 1
                if mine[i - 1][j + 1] == '*': cnt += 1
                if mine[i][j + 1] == '*': cnt += 1
                if mine[i + 1][j + 1] == '*': cnt += 1
                if mine[i + 1][j] == '*': cnt += 1
                if mine[i + 1][j - 1] == '*': cnt += 1
                if mine[i][j - 1] == '*': cnt += 1
            line += str(cnt)
        else:
            line += '.'
    print(line)