def permutation(a, n):
    result = []

    if n == 0:
        return [[]]

    for i, elem in enumerate(a):
        for per in permutation(a[:i] + a[i+1:], n-1):
            result += [[elem] + per]
    return result

from sys import stdin

num = int(stdin.readline())
arr = [i for i in range(1, num+1)]

for i in permutation(arr, num):
    print(*i)
