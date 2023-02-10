from sys import stdin

tot = 0

for _ in range(5):
    n = int(stdin.readline())
    tot += n if n > 40 else 40

print(tot//5)