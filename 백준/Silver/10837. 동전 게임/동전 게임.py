from sys import stdin

k = int(stdin.readline())

for _ in range(int(stdin.readline())):
    m, n = map(int, stdin.readline().split())

    if m == n:
        print(1)
        continue

    remainGame = k - max(n, m)
    gap = abs(m-n)

    if m > n:
        if gap - remainGame <= 2:
            print(1)
        else:
            print(0)
        continue

    if gap - remainGame <= 1:
        print(1)
        continue
    print(0)