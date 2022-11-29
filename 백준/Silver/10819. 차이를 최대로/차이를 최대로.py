from sys import stdin


def back(x):

    if x == n:
        result.append(sum(abs(arr[temp[i+1]] - arr[temp[i]]) for i in range(n-1)))
        return

    for i in range(n):
        if i not in temp:
            temp.append(i)
            back(x+1)
            temp.pop()


n = int(stdin.readline())
arr = sorted(list(map(int, stdin.readline().split())))
result = []
temp = []
back(0)
print(max(result))