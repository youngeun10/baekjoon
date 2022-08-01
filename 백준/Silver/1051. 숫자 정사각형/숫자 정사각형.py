from sys import stdin as std

n, m = map(int, std.readline().split())
a = []

for i in range(n):
    a.append(list(std.readline().strip()))

chk = 0

if n == 1 or m == 1:
    print(1)
    quit()

for i in range(min(n, m), 1, -1):
    for x in range((n-i)+1):
        for y in range((m-i)+1):
            if a[x][y] == a[x][y+(i-1)] == a[x+(i-1)][y] == a[x+(i-1)][y+(i-1)]:
                print(i*i)
                chk = 1
                quit()

print(1) if chk == 0 else quit()