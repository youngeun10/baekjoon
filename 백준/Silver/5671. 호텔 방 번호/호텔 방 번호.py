def check(t):
    tmp = str(t)
    for i in tmp:
        if tmp.count(i) > 1:
            return 0
    return 1


while True:
    try:
        n, m = map(int, input().split())
        print(sum(check(x) for x in range(n, m + 1)))
    except:
        break

