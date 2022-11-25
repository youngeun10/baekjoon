from sys import stdin

a, b = map(str, stdin.readline().split())
result = 0

if a in b:
    print(0)
    exit()

al, bl = [], []
for i in a:
    al.append(ord(i))
for i in b:
    bl.append(ord(i))

for i in range(len(b)-len(a)+1):
    tmp = bl[i:(i+len(a)+1)]
    cl = [tmpi-ai for ai, tmpi in zip(al, tmp)]
    result = max(result, cl.count(0))
print(len(a)-result)