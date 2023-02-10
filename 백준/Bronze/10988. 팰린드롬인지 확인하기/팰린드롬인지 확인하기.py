from sys import stdin

t = stdin.readline().rstrip()

for i in range(len(t)//2):
    if t[i] != t[len(t)-1-i]:
        print(0); exit()
print(1)