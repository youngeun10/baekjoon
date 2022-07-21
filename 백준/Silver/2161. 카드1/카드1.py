import collections

n = int(input())
arr = collections.deque([i for i in range(1, n+1)])
trash = []
for _ in range(n):
    trash.append(arr.popleft())
    arr.rotate(-1)
print(*trash)