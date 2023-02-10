from sys import stdin

a, b, c = map(int, stdin.readline().split())
print((a*b)-c) if (a*b)-c >= 0 else print(0)