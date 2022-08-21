from sys import stdin

a, b = map(int, stdin.readline().rstrip().split())
n = int(stdin.readline().rstrip())

chk = []
cnt = 1

for _ in range(n):
    f = int(stdin.readline().rstrip())
    chk.append(abs(b - f))

if min(chk) == 0:
    print(cnt)
else:
    print(cnt + min(chk)) if abs(b-a) > min(chk) else print(abs(b-a))