def find(parent, x):
    if parent[x] == x:
        return x
    return find(parent, parent[x])

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)

    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

import sys
input = sys.stdin.readline

V, E = map(int, input().split())
parent = [i for i in range(V+1)]

edges = []
result = 0

for _ in range(E):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost

print(result)