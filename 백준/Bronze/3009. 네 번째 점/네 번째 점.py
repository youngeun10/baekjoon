from sys import stdin

x = {}
y = {}

for _ in range(3):
    xt, yt = map(int, stdin.readline().split())

    if xt not in x:
        x[xt] = 1
    else:
        x[xt] += 1

    if yt not in y:
        y[yt] = 1
    else:
        y[yt] += 1

result = []
for i in x:
    if x[i] == 1:
        result.append(i)
for i in y:
    if y[i] == 1:
        result.append(i)
print(*result)