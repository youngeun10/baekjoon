# 에라토스테네스의 체
import sys

N, K = map(int, sys.stdin.readline().split())
numChk = [i for i in range(N+1)]
cnt = 1

for i in range(2, N+1):
    n = i
    while n <= N:
        if numChk[n] != 0:
            if cnt == K:
                print(n)
                exit()
            cnt += 1
            numChk[n] = 0
        n += i