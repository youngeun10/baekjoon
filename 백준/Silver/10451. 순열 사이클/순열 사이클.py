import sys
from collections import defaultdict
sys.setrecursionlimit(10**9)

t = int(sys.stdin.readline())


def dfs(start, curr):
    if start == curr and visited[curr]:
        global answer
        answer += 1
        return

    visited[curr] = True
    for next_node in graph[curr]:
        dfs(start, next_node)


for _ in range(t):
    n = int(sys.stdin.readline())
    answer = 0
    graph = defaultdict(list)
    visited = [False] * (n + 1)
    nums = list(map(int, sys.stdin.readline().split()))
    for idx, num in enumerate(nums):
        graph[idx + 1].append(num)
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, i)
    print(answer)
