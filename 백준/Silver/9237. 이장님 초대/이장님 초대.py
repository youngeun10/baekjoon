from sys import stdin
n = int(stdin.readline())
tree = list(map(int, stdin.readline().rstrip().split()))
days = {}
tree.sort(reverse=True)
for i in range(len(tree)):
    days[tree[i]] = (i+1) + tree[i] + 1
print(max(days.values()))