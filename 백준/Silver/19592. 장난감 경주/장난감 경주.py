from sys import stdin

for _ in range(int(stdin.readline())):
    n, x, y = map(int, stdin.readline().rstrip().split())
    v = list(map(int, stdin.readline().rstrip().split()))

    result = []
    a = x / max(v)
    for i in reversed(range(y+1)):
        if max(v) == v[-1]:
            result.append(0)
            break
        m = ((x-i) / v[-1]) + 1
        if m >= a:
            break
        else:
            result.append(i)

    print(-1) if len(result) == 0 else print(min(result))