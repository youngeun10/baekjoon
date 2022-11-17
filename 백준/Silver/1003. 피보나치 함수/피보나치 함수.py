from sys import stdin

n = int(stdin.readline())
arr = [int(stdin.readline().rstrip()) for _ in range(n)]
fibo = [(1, 0), (0, 1)]

for i in range(2, max(arr)+1):
    tmp = tuple(sum(elem) for elem in zip(fibo[i-1], fibo[i-2]))
    fibo.append(tmp)

for n in arr:
    a, b = fibo[n]
    print(a, b)