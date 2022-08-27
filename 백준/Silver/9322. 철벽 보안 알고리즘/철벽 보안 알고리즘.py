from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    key1 = tuple(stdin.readline().rstrip().split())
    key2 = tuple(stdin.readline().rstrip().split())
    s = []
    for i in key1:
        s.append(key2.index(i))
    code = tuple(stdin.readline().rstrip().split())

    for i in s:
        print(code[i], end=' ')
    print()