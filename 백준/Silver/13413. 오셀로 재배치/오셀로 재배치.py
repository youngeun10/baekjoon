from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())

    tmp = list(stdin.readline().rstrip())
    org = list(stdin.readline().rstrip())
    b = []

    for t, o in zip(tmp, org):
        if o != t:
            b.append(o)

    if len(b) == 0:
        print(0)
        continue
    if b.count('B') > b.count('W'):
        print(b.count('B'))
    else:
        print(b.count('W'))