from sys import stdin

for _ in range(int(stdin.readline())):
    h, w = map(int, stdin.readline().rstrip().split())
    tmp = {}

    for i in range(h):
        f = list(map(int, stdin.readline().rstrip().split()))
        for j in range(len(f)):
            if f[j] != -1:
                tmp[f[j]] = (i+1, j+1)      # 층, 호
    floor = sorted(tmp.items())

    hh = [1] * (h+1)
    result = 0

    for i, j in floor:
        result += 20 * abs(1 - j[0])
        c = [abs(hh[j[0]] - j[1]), abs(w - abs(hh[j[0]] - j[1]))]
        result += 5 * min(c)
        hh[j[0]] = j[1]
    print(result)