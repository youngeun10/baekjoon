from sys import stdin

n = int(stdin.readline())
m, k = map(int, stdin.readline().split())
pen = list(map(int, stdin.readline().split()))
pen.sort(reverse=True)

penT = m * k
if sum(pen) < penT: print("STRESS"); exit()
cnt = 0

for i in pen:
    if penT > 0:
        cnt += 1
        penT -= i
    else:
        break

print(cnt)