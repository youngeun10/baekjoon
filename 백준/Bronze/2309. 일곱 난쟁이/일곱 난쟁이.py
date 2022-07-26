from sys import stdin
arr = []

for _ in range(9):
    arr.append(int(stdin.readline().strip()))
arr.sort()

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        tmp = arr[:]
        tmp[i] = 0
        tmp[j] = 0
        if sum(tmp) == 100:
            for a in tmp:
                if a != 0:
                    print(a)
            quit()