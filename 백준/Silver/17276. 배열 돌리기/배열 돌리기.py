import sys
input = sys.stdin.readline
import copy

def rotate(n):      # 돌릴 것 완성
    hn = n // 2
    tmp = [[0] * n for _ in range(n)]
    for i in range(1, hn+1):
        tmp[hn-i][hn-i], tmp[hn-i][hn] = [0, i], [0, i]
        tmp[hn-i][hn+i], tmp[hn][hn+i] = [i, 0], [i, 0]
        tmp[hn+i][hn], tmp[hn+i][hn+i] = [0, -i], [0, -i]
        tmp[hn][hn-i], tmp[hn+i][hn-i] = [-i, 0], [-i, 0]
    return tmp

T = int(input())        # 테스트 케이스
result = []
for _ in range(T):
    N, D = map(int, input().split())        # N, 각도

    ARR = [list(map(int, input().split())) for _ in range(N)]       # 배열 저장
    rot = (D % 360) // 45
    pD = rotate(N)

    tmp = ARR
    for _ in range(rot):
        tmp1 = copy.deepcopy(tmp)
        for r in range(N):
            for c in range(N):
                if pD[r][c] == 0:
                    continue
                dr, dc = pD[r][c]
                tmp1[r+dr][c+dc] = tmp[r][c]
        tmp = tmp1

    for i in range(N):
        print(*tmp[i])