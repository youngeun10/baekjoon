def bfs(graph, v, checked):
    global cnt

    if not checked[v]:
        checked[v] = True
        cnt += 1

    for i in graph[v]:
        if not checked[i]:
            bfs(graph, i, checked)


import sys
input = sys.stdin.readline

comN = int(input()) + 1
visited = [False] * comN
network = {}
for i in range(1, comN):
    network[i] = []
cnt = 0

for _ in range(int(input())):
    s, e = map(int, input().split())

    network[s].append(e)
    network[e].append(s)

bfs(network, 1, visited)
print(cnt-1)