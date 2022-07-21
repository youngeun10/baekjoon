from sys import stdin

arr = []

for _ in range(int(stdin.readline().strip())):
    n = int(stdin.readline().strip())
    arr.pop() if n == 0 else arr.append(n)

print(sum(arr))