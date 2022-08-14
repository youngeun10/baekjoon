from sys import stdin
pronounce = ["pi", "ka", "chu"]
n = stdin.readline().rstrip()
for i in pronounce:
    n = n.replace(i, '-')
n = n.replace('-', '')
print("YES") if len(n) == 0 else print("NO")