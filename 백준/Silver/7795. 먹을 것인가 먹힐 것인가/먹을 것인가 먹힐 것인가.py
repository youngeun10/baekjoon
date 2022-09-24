from sys import stdin

for _ in range(int(stdin.readline())):
    n, m = map(int, stdin.readline().rstrip().split())

    nArr = list(map(int, stdin.readline().rstrip().split()))
    mArr = list(map(int, stdin.readline().rstrip().split()))

    nCnt = [0] * n

    nArr.sort()
    mArr.sort()

    for i in range(n):
        if i != 0:
            nCnt[i] = nCnt[i-1]
        for j in range(nCnt[i-1], m):
            if nArr[i] <= mArr[j]:
                break
            else:
                nCnt[i] += 1
    print(sum(nCnt))