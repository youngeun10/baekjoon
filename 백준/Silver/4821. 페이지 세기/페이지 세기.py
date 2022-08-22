from sys import stdin

while True:
    n = int(stdin.readline().rstrip())
    if n == 0:
        break

    p = [0] * (n+1)
    chk = stdin.readline().rstrip().split(',')

    for s in chk:
        if '-' in s:
            a, b = map(int, s.split('-'))
            if n >= a:
                if a <= b:
                    if b > n: b = n
                    for j in range(a, b+1):
                        p[j] = 1
        else:
            if n >= int(s):
                p[int(s)] = 1
    print(sum(p))