from sys import stdin

s = stdin.readline().rstrip()
text = stdin.readline().rstrip()

s = s.replace(text, '-')

print(s.count('-'))