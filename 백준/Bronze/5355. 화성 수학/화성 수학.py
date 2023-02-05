for _ in range(int(input())):
    tmp = list(map(str, input().split()))
    n = 0
    for t in tmp:
        if t == '@':
            n *= 3
        elif t == '%':
            n += 5
        elif t == '#':
            n -= 7
        else:
            n = float(t)

    print("{:.2f}".format(n))