from sys import stdin
n = int(stdin.readline())
enter_list = dict()
for _ in range(n):
    n, s = map(str, input().split())
    if s == "enter":
        enter_list[n] = s
    else:
        del enter_list[n]
enter_list = sorted(enter_list.keys(), reverse=True)
print(*enter_list, sep='\n')
