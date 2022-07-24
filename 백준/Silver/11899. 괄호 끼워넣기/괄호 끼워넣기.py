from sys import stdin

s = stdin.readline().strip()
arr = []

for i in s:
    if arr:
        if i == '(':
            arr.append(i)
        else:
            arr.pop() if arr[-1] == '(' else arr.append(i)
    else:
        arr.append(i)
print(len(arr))