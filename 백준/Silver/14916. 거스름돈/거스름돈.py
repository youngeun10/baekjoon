from sys import stdin

n = int(stdin.readline())
r = []

if n == 1 or n == 3:
    print(-1)
    quit()

if n % 2 == 0:
    r.append(n//2)

for i in range(1, (n//5)+1):
    tmp = i
    tmp += (n - (5*i)) / 2

    if int(tmp) == tmp:
        r.append(int(tmp))

print(min(r))