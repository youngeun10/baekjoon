from sys import stdin

n = int(stdin.readline())
num = list(map(int, stdin.readline().split()))
result = []

for k in num:
    print(1, end=' ') if int((k ** 0.5)) ** 2 == k else print(0, end=' ')