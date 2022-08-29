from sys import stdin

n = int(stdin.readline())
chk = 64
cnt = 0
while n > 0:
    if n // chk > 0:
        n -= chk
        cnt += 1
    chk //= 2
print(cnt)