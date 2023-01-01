from sys import stdin

area = [[0] * 100 for _ in range(100)]

for _ in range(int(stdin.readline())):
    x, y = map(int, stdin.readline().split())

    for i in range(x-1, x+9):
        for j in range(y-1, y+9):
            area[i][j] = 1

result = 0
for i in range(100):
    result += sum(area[i])
print(result)