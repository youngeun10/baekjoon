from sys import stdin
from math import gcd

n = int(stdin.readline())

for _ in range(n):
    arr = list(map(int, stdin.readline().split()))
    cnt = 0
    for i in range(1, len(arr)):
        for j in range(i+1, len(arr)):
            cnt += gcd(arr[i], arr[j])
    print(cnt)