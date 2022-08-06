from sys import stdin

iN, oN = map(int, stdin.readline().rstrip().split())
note = {}

for _ in range(iN):
    s, pw = map(str, stdin.readline().rstrip().split())
    note[s] = pw

for _ in range(oN):
    print(note[stdin.readline().rstrip()])