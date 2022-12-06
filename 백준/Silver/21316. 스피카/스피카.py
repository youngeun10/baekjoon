from sys import stdin
dic = {}
arr = []

for _ in range(12):
    x, y = map(int, stdin.readline().split())

    if x in dic:
        dic[x].append(y)
    else:
        dic[x] = [y]
    if y in dic:
        dic[y].append(x)
    else:
        dic[y] = [x]

for i in dic:
    if len(dic[i]) == 3:
        arr.append(i)
for i in arr:
    sum = 0
    for j in dic[i]:
        sum += len(dic[j])
    if sum == 6:
        print(i)
        break