from sys import stdin

for _ in range(int(stdin.readline())):
    r, e, c = map(int, stdin.readline().split())

    if r == (e-c):
        print("does not matter")
    elif r < (e-c):
        print("advertise")
    else:
        print("do not advertise")