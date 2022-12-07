from sys import stdin

for _ in range(int(stdin.readline())):
    s = list(map(str, stdin.readline().split()))
    result, a = [], []
    while True:
        tmp = list(map(str, stdin.readline().split()))

        if len(tmp) > 3:
            break
        a.append(tmp[2])

    for t in s:
        if t not in a:
            result.append(t)
    print(*result)