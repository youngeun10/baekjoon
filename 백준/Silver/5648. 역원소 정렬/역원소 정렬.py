from sys import stdin


def changeNum(num):
    if len(num) == 1:
        return int(num)
    tmp = 0
    c = 1
    for i in num:
        tmp += (int(i)*c)
        c *= 10
    return tmp

v = list(map(str, stdin.readline().split()))
n = int(v[0])
cnt = len(v) - 1
val = []

for i in range(1, len(v)):
    val.append(changeNum(v[i]))

while cnt < n:
    v = list(map(str, stdin.readline().split()))

    for i in v:
        val.append(changeNum(i))
        cnt += 1

val.sort()
print(*val, sep='\n')