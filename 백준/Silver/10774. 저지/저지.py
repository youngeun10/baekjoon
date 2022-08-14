from sys import stdin
size = "SML"
j = int(stdin.readline())
a = int(stdin.readline())
goods = {}
needs = {}
cnt = 0
for i in range(j):
    n = stdin.readline().rstrip()
    goods[str(i+1)] = n
for i in range(a):
    tmp = tuple(map(str, stdin.readline().rstrip().split()))
    needs[tmp[1]] = [size[x] for x in range(size.find(tmp[0]), len(size))]
    if tmp[1] in goods.keys():
        if goods[tmp[1]] in needs[tmp[1]]:
            cnt += 1
            goods[tmp[1]] = 0
print(cnt)