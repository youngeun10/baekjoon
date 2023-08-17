import sys
yin = sys.stdin.readline

N = int(yin())
INF = int(1e8)
dp = [[-1 for _ in range(1<<N)] for _ in range(N)]     # 2 ** N 개만큼 컬럼을 만들어 줌.

def dfs(cur, visited):
    # all node visit
    if visited == (1 << N) - 1:     # 모든 도시를 방문 했다면
        if graph[cur][0] == 0:      # 출발 점으로 가는 경로가 없을 때
            return INF
        dp[cur][visited] = graph[cur][0]
        return graph[cur][0]        # 츨발 점으로 가는 경로가 있을 때

    # memoization
    if dp[cur][visited] != -1:       # 이미 최소 비용이 계산 되어 있댜면
        return dp[cur][visited]

    min_dist = INF
    for i in range(1, N):           # 모든 도시를 탐방
        # if not visited i-node yet + graph not zero
        if not visited & (1 << i) and graph[cur][i] != 0:
             min_dist = min(min_dist, dfs(i, visited | (1 << i)) + graph[cur][i])

    dp[cur][visited] = min_dist
    return dp[cur][visited]

graph = []
for i in range(N):
    graph.append(list(map(int, yin().split())))

print(dfs(0, 1))