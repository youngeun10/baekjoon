import sys
input = sys.stdin.readline
result = []

def numCnt(a, nArr):
    cnt = 0
    for n in nArr:
        if n > a:
            cnt += 1
    return (cnt / len(nArr))  * 100

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    avg = sum(arr[1:]) / arr[0]

    result.append("%.3f" %numCnt(avg, arr[1:]))

print(*result, sep="%\n", end="%")