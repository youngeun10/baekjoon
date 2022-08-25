from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    nArr = set(map(int, stdin.readline().rstrip().split()))
    m = int(stdin.readline())
    mArr = list(map(int, stdin.readline().rstrip().split()))

    for i in mArr:
        print(1) if i in nArr else print(0)