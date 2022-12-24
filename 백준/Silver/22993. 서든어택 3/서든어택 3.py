from sys import stdin

n = int(stdin.readline())
attack = list(map(int, stdin.readline().split()))
atttmp = sorted(attack[1:])
jw = attack[0]

for i in atttmp:
    if i < jw:
        jw += i
    else:
        print("No")
        exit()
print("Yes")