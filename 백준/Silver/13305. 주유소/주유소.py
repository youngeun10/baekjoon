import sys

n = int(sys.stdin.readline())
dis = list(map(int, sys.stdin.readline().strip().split()))
oil = list(map(int, sys.stdin.readline().strip().split()))
result = 0
low_price = oil[0]

for i in range(0, n-1):
    if low_price > oil[i]:
        low_price = oil[i]
    result += low_price * dis[i]
print(result)