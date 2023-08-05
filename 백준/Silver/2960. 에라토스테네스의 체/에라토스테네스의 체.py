import sys

# N: 범위의 끝 수, K: 구하고 싶은 번째
N, K = map(int, sys.stdin.readline().split())
numChk = [True] * (N+1)         # 값이 해당 되었는지 확인하는 리스트
cnt = 1

for i in range(2, N+1):
    v = i
    while v <= N:
        if numChk[v]:
            numChk[v] = False
            if cnt == K: print(v); exit()
            cnt += 1
        v += i