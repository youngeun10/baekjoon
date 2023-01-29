from sys import stdin

n = int(stdin.readline())
r = (n//5) + 1
c = (n//3) + 1
result = 10**9

for i in range(r):
    for j in range(c):
        if (i*5) + (j*3) == n:
            result = min(i+j, result)

print(-1) if result == 10**9 else print(result)