from sys import stdin

A = int(stdin.readline())

for i in range(1, A + 1):
    gap = i + 1

    if 30 % gap == 0:
        print(i)