import sys

n = int(sys.stdin.readline().strip())

for _ in range(n):
    a = int(sys.stdin.readline().strip())
    x = 2
    cnt = []
    while a != 1:
        if a % x == 0:
            a = a // x
            cnt.append(x)
        else:
            x += 1

    tmp = list(set(cnt))
    tmp.sort()
    for i in tmp:
        print(i, cnt.count(i))
