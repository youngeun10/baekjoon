from sys import stdin
import math

n = int(stdin.readline())
m = int(stdin.readline())
x = list(map(int, stdin.readline().rstrip().split()))
h = [x[0], n-x[-1]]
s = x[0]

for i in range(1, m):
    h.append(math.ceil((x[i]-s)/2))
    s = x[i]

print(max(h)) if m != 1 else print(n)