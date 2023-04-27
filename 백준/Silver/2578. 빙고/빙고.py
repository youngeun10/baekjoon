def bingoConfirm(b):
    result = 0

    for i in range(5):
        if sum(b[i]) == 0:
            result += 1

    for j in range(5):
        s = 0
        for i in range(5):
            s += b[i][j]
        if s == 0:
            result += 1

    x = 0
    y = 0
    for i in range(5):
        x += b[i][i]
        y += b[i][4-i]

    if x == 0: result += 1
    if y == 0: result += 1

    return result

def bingoDelete(bingo, v):

    for i in range(5):
        for j in range(5):
            if bingo[i][j] == v:
                bingo[i][j] = 0
                return

import sys
input = sys.stdin.readline

bingo = [list(map(int, input().split())) for _ in range(5)]
answer = []
for _ in range(5):
    answer += list(map(int, input().split()))

for i in range(25):

    bingoDelete(bingo, answer[i])

    if i >= 11 and bingoConfirm(bingo) >= 3:
        print(i+1)
        exit()