from sys import stdin

h, m, s = map(int, stdin.readline().split())
t = int(stdin.readline())
t += (h*3600) + (m*60) + s
h = (t//3600) % 24 if t // 3600 > 23 else t // 3600
tmp = t % 3600
m = tmp // 60
s = tmp % 60
print(h, m, s)