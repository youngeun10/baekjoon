from sys import stdin

score = []

for i in range(1, 9):
    score.append((i, int(stdin.readline())))

score.sort(key=lambda x: x[1])
tot = 0
result = []

for i in range(3, 8):
    tot += score[i][1]
    result.append(score[i][0])

print(tot)
print(*sorted(result))