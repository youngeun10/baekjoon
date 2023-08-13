import sys
input = sys.stdin.readline
from collections import deque

N = int(input())        # N 입력
grim = [list(input().rstrip()) for _ in range(N)]       # 그림 입력

def solution(info):
    visited = [[False] * N for _ in range(N)]       # 방문 정보르 저장
    dirc = [(0, 1), (0, -1), (-1, 0), (1, 0)]       # 동서남북 방향 설정
    cnt = 0

    for r in range(N):
        for c in range(N):
            if visited[r][c]:
                continue
            visited[r][c] = True
            color = grim[r][c]
            cnt += 1
            queue = deque([(r, c)])  # queue를 설정
            while queue:
                _r, _c = queue.popleft()
                for dr, dc in dirc:
                    x, y = _r + dr, _c + dc
                    if not (0 <= x < N and 0 <= y < N) or visited[x][y] or grim[x][y] in info[color]:
                        continue
                    queue.append((x, y))
                    visited[x][y] = True
    return cnt

diff_color1 = {"R": {"G", "B"}, "G": {"R", "B"}, "B": {"R", "G"}}
diff_color2 = {"R": {"B"}, "G": {"B"}, "B": {"R", "G"}}

print(solution(diff_color1), solution(diff_color2))