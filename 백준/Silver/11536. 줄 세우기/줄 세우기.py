from sys import stdin

n = int(stdin.readline())
name = [stdin.readline().rstrip() for _ in range(n)]

if name == sorted(name):
    print("INCREASING")
elif name == sorted(name, reverse=True):
    print("DECREASING")
else:
    print("NEITHER")