import sys
input = sys.stdin.readline

n = int(input())
start, end = 0, 2 ** 63
chk = 2 ** 63

while start <= end:
    mid = (start + end) // 2

    if mid * mid >= n:
        end = mid - 1
        chk = min(chk, mid)
    else:
        start = mid + 1

print(chk)