from sys import stdin

n = int(stdin.readline())
nArr = [i for i in range(1, n+1)]
r = 0
p = 0

while len(nArr) != 1:
    r += 1
    p += (r ** 3) - 1
    p = p % len(nArr)
    nArr.pop(p)
    
print(nArr[0])
