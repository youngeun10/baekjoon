from sys import stdin

n = int(stdin.readline())
t = stdin.readline()

if t.count('A') == t.count('B'):
    print("Tie")
elif t.count('A') > t.count('B'):
    print('A')
else:
    print('B')