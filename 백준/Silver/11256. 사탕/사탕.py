from sys import stdin

for _ in range(int(stdin.readline())):
    j, n = map(int, stdin.readline().rstrip().split())
    box = []
    cnt = 0
    for _ in range(n):
        a, b = map(int, stdin.readline().rstrip().split())
        box.append(a*b)
    box.sort(reverse=True)

    for i in box:
        if j <= 0:
            print(cnt)
            break
        else:
            j -= i
            cnt += 1