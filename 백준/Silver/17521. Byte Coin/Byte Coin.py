from sys import stdin

n, money = map(int, stdin.readline().split())
graph = [int(stdin.readline()) for _ in range(n)]
floor = graph[0]
ceiling = graph[0]

for i in range(1, n):
    if ceiling > graph[i]:
        s = money // floor
        money -= (floor * s)
        money += (ceiling * s)
        floor = ceiling
        ceiling = 0
    elif ceiling < graph[i]:
        ceiling = graph[i]

    if floor > graph[i]:
        floor = graph[i]

if floor < ceiling:
    s = money // floor
    money -= (floor * s)
    money += (ceiling * s)

print(money)