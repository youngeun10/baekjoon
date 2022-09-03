from sys import stdin

n = int(stdin.readline())
s = list(map(int, stdin.readline().rstrip().split()))
s = sorted(s)
tot = sum(s)
result = 0
for i in s:
    tot -= i
    result += i * tot
print(result)