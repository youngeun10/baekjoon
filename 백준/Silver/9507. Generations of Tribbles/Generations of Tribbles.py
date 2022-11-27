from sys import stdin

t = int(stdin.readline())
arr = [int(stdin.readline()) for _ in range(t)]
koong = [1, 1, 2, 4]

for i in range(4, max(arr)+1):
    koong.append(koong[i-1] + koong[i-2] + koong[i-3] + koong[i-4])

for i in arr:
    print(koong[i])