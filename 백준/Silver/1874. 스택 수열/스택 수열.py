from sys import stdin

n = int(stdin.readline())
arr = [int(stdin.readline().rstrip()) for _ in range(n)]
idx = 0
stk = []
result = []

for i in range(1, n+1):
    stk.append(i)
    result.append('+')
    while stk:
        if arr[idx] == stk[-1]:
            result.append('-')
            stk.pop()
            idx += 1
        else:
            break

print(*result, sep='\n') if idx == n else print("NO")