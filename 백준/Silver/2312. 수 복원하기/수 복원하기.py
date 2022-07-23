def reconstruction(num):
    x = 2
    dic = {}
    while num != 1:
        if num % x == 0:
            if x in dic:
                dic[x] += 1
            else:
                dic[x] = 1
            num //= x
        else:
            x += 1
    return dic

import sys

n = int(sys.stdin.readline().strip())

for _ in range(n):
    d = reconstruction(int(sys.stdin.readline().strip()))
    for k, v in d.items():
        print(k, v)
