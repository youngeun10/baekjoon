from sys import stdin

n, m = map(int, stdin.readline().split())
chk = 1
for _ in range(m):      # 값 넣기
    heap = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))

    for i in range(1, heap):
        if a[i-1] < a[i]:
            chk = 0

print("No") if chk == 0 else print("Yes")