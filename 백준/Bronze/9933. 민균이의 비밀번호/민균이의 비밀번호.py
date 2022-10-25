from sys import stdin

n = int(stdin.readline())
arr = [stdin.readline().rstrip() for _ in range(n)]

for i in arr:
    tmp = i[::-1]
    if tmp in arr:
        print(len(tmp), i[len(tmp)//2])
        break