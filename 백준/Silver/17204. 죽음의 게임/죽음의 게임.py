import sys
from collections import deque

def bfs(v):
    queue = deque([v])
    cnt = 0
    for _ in range(n):
        target = queue.popleft()
        cnt += 1
        
        if graph[target] == k:
            return cnt
        
        queue.append(graph[target])
    return -1


n, k = map(int, sys.stdin.readline().split())
graph = [int(sys.stdin.readline()) for _ in range(n)]

print(bfs(0))