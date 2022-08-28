from sys import stdin

n = int(stdin.readline())
enter = {}
for _ in range(n):
    tmp = stdin.readline().rstrip()
    if tmp not in enter:
        enter[tmp] = 1
    else:
        enter[tmp] += 1

for _ in range(n-1):
    enter[stdin.readline().rstrip()] -= 1
result = dict(map(reversed, enter.items()))
print(result[1])