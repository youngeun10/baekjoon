from sys import stdin

s = list(stdin.readline().rstrip())
for i in s:
    if 'a' <= i <= 'z':
        print(chr(ord(i) - 32), end='')
    else:
        print(chr(ord(i) + 32), end='')