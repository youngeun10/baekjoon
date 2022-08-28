from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().rstrip().split()))
    s = [0]*n
    s[0] = arr[0]

    for i in range(1, n):
        s[i] = max(s[i-1]+arr[i], arr[i])
    print(max(s))