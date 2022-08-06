from sys import stdin

n = int(stdin.readline().rstrip())
nArr = [1, 1]
for i in range(1, n):
    nArr.append(nArr[i]+nArr[i-1])

print(2*nArr[-1]+2*nArr[-2])