from sys import stdin

s = int(stdin.readline())
tot = 0
n = 1

while tot < s:
    tot += n
    n += 1

print(n-2) if tot != s else print(n-1)