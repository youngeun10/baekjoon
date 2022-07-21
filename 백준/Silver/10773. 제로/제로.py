n = int(input())
arr = []

for _ in range(n):
    n = int(input())
    arr.pop() if n == 0 else arr.append(n)

print(sum(arr))