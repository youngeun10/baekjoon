import sys

def main():
    N = int(sys.stdin.readline())
    graph = [ [] for _ in range(N+1)]
    for _ in range(N-1):
        x, y = map(int, sys.stdin.readline().split())
        graph[x].append(y)
        graph[y].append(x)

    parents = [0] * (N+1)
    stack = [1]

    while stack:
        node = stack.pop()
        for next_node in graph[node]:
            if next_node != parents[node]:
                parents[next_node] = node
                stack.append(next_node)
    print(*parents[2:], sep="\n")


if __name__ == "__main__":
    main()