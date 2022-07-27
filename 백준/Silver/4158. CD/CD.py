from sys import stdin

while True:
    n, m = map(int, stdin.readline().split())

    if n == m == 0:
        break

    sg = [int(stdin.readline().strip()) for _ in range(n)]
    sy = [int(stdin.readline().strip()) for _ in range(m)]

    print(len(sg+sy) - len(set(sg+sy)))