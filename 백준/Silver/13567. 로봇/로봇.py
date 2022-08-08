from sys import stdin

way = [[1, 0], [0, 1], [-1, 0], [0, -1]]
c = 0
a = 0
b = 0

sq, op = map(int, stdin.readline().rstrip().split())
for _ in range(op):
    s, v = map(str, stdin.readline().rstrip().split())
    if s == "MOVE":
        a += way[c][0] * int(v)
        b += way[c][1] * int(v)
    else:
        if v == '1':
            c += -1
        else:
            c += 1
        c = c % 4
    if 0 <= a <= sq and 0 <= b <= sq: 
        continue
    else: 
        print(-1) 
        quit()
print(a, b)