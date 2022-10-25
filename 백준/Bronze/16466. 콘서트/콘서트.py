from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
arr.sort()
chk = 1

for i in range(1, arr[-1]):
    if arr[i-1] != i:
        print(i)
        exit()       

print(arr[-1]+1)