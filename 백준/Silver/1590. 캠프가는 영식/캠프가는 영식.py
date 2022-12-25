from sys import stdin

n, ys = map(int, stdin.readline().split())
result = 2 ** 31

for r in range(n):
    # s: 시작시간, i: 간격, c: 대수
    s, i, c = map(int, stdin.readline().split())

    for a in range(c):
        tmp = (s + (i*a)) - ys
        if tmp == 0:
            result = 0
        elif tmp > 0:
            result = min(tmp, result)

print(result) if result < 2**31 else print(-1)