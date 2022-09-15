from sys import stdin

n, a, d = map(int, stdin.readline().rstrip().split())
arr = list(map(int, stdin.readline().rstrip().split()))
cnt = 0

for i in arr:
    if i == a + (cnt*d):
        cnt += 1

print(cnt)