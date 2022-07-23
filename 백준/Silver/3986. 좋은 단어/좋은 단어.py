import sys

n = int(sys.stdin.readline().strip())
cnt = 0
for _ in range(n):
    s = sys.stdin.readline().strip()
    result = []

    for i in s:

        if len(result) == 0:
            result.append(i)
        else:
            if result[len(result)-1] == i:
                result.pop()
            else:
                result.append(i)

    if len(result) == 0:
        cnt += 1
print(cnt)
