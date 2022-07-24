from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
temp = []

for i in range(n):
    t = i - arr[i]

    f = temp[0:t]
    e = temp[t:i+1]

    temp = []
    temp.extend(f)
    temp.append(i+1)
    temp.extend(e)

print(*temp)