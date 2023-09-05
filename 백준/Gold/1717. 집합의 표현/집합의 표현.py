import sys
yin = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def find(x, parent):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x], parent)
    return find(parent[x], parent)

def union(s, e, parent):
    s = find(s, parent)
    e = find(e, parent)
    if s < e:
        parent[e] = s
    else:
        parent[s] = e

def solution():
    N, M = map(int, yin().split())
    parent = {i:i for i in range(N+1)}
    inputCase = [list(map(int, yin().split())) for _ in range(M)]
    result = []

    for c, a, b in inputCase:
        if c:
            if find(a, parent) == find(b, parent):
                result.append("YES")
            else:
                result.append("NO")
        else:
            union(a, b, parent)
    return result

print(*solution(), sep="\n")