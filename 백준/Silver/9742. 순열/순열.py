from sys import stdin
from math import factorial as f

def back():
    if len(tmp) == len(s):
        result.append(''.join(tmp))
        return

    for i in range(len(s)):
        if visited[i] == False:
            tmp.append(s[i])
            visited[i] = True
            back()
            visited[i] = False
            tmp.pop()

while True:
    input_data = stdin.readline().rstrip().split()

    if len(input_data) != 2:
        break

    s, n = input_data
    n = int(n)

    if f(len(s)) < n:
        print(f'{s} {n} = No permutation')
    else:
        tmp = []
        result = []
        visited = [False] * len(s)

        back()

        print(f'{s} {n} = {result[n-1]}')
