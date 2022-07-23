import sys

card = sys.stdin.readline().strip()
cnt = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        , [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        , [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        , [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    ]
result = []

for i in range(len(card)//3):

    if card[(i*3)] == 'P':
        sign = 0
        n = int(card[(i * 3) + 1:(i * 3) + 3])
    elif card[(i*3)] == 'K':
        sign = 1
        n = int(card[(i * 3) + 1:(i * 3) + 3])
    elif card[(i*3)] == 'H':
        sign = 2
        n = int(card[(i * 3) + 1:(i * 3) + 3])
    elif card[(i*3)] == 'T':
        sign = 3
        n = int(card[(i * 3) + 1:(i * 3) + 3])

    if n in cnt[sign]:
        cnt[sign].remove(n)
    else:
        print("GRESKA")
        quit()

for i in range(4):
    result.append(len(cnt[i]))
print(*result)
