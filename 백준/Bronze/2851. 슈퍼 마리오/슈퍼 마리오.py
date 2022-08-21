from sys import stdin

n = [int(stdin.readline().rstrip()) for _ in range(10)]
s = []
gap = []
result = 100

for i in range(10):
    s.append(sum(n[:i+1]))
    gap.append(abs(100 - sum(n[:i+1])))
gap.sort()

if gap[0] == 0:
    print(100)
else:
    print(100+gap[0]) if gap[0] + 100 in s else print(100-gap[0])