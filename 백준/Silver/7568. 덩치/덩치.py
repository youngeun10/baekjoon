from sys import stdin

n = int(stdin.readline().rstrip())
data = []
rank = []
for _ in range(n):
    w, h = map(int, stdin.readline().rstrip().split())
    data.append((w, h))

for i in range(n):
    r = 1
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            r += 1
    rank.append(r)
print(*rank)