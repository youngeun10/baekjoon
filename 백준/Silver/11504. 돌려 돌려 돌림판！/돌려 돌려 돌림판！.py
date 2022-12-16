from sys import stdin

# 리스트를 숫자로 만드는 함수
def changeInt(a, l):
    n = 0
    for i in range(l):
        n += (10 ** (l - i - 1)) * a[i]
    return n


for _ in range(int(stdin.readline())):
    n, m = map(int, stdin.readline().split())
    x = changeInt(list(map(int, stdin.readline().split())), m)
    y = changeInt(list(map(int, stdin.readline().split())), m)

    numArr = list(map(int, stdin.readline().split()))
    numArr = numArr + numArr[:m]
    result = 0

    for i in range(n):
        tmp = changeInt(numArr[i:(i+m)], m)
        if x <= tmp <= y:
            result += 1
    print(result)