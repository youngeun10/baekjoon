from sys import stdin

a, b, c = map(int, stdin.readline().split())
n = int(stdin.readline())

result = [-1] * (a+b+c+1)
arrI = [0] * n
arrJ = [0] * n
arrK = [0] * n
arrR = [0] * n


def inspction():
    sum = 0

    for j in range(n):
        if arrR[j] == 0:
            idx = result[arrI[j]] + result[arrJ[j]] + result[arrK[j]]
            if idx == 1:
                if result[arrI[j]] == -1:
                    result[arrI[j]] = 0
                elif result[arrJ[j]] == -1:
                    result[arrJ[j]] = 0
                elif result[arrK[j]] == -1:
                    result[arrK[j]] = 0

    for k in range(1, a+b+c+1):
        if result[k] == -1: result[k] = 2


for i in range(n):

    arrI[i], arrJ[i], arrK[i], arrR[i] = map(int, stdin.readline().split())

    if arrR[i] == 1:
        result[arrI[i]] = 1
        result[arrJ[i]] = 1
        result[arrK[i]] = 1

inspction()

for k in range(1, a+b+c+1):
    print(result[k])