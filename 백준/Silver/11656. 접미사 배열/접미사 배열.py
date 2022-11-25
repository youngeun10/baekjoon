from sys import stdin

s = stdin.readline().rstrip()
d = []

for i in range(len(s)):
    d.append(str(s[i:]))

d.sort()
print(*d, sep='\n')