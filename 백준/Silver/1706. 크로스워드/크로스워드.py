from sys import stdin

x, y = map(int, stdin.readline().rstrip().split())
word = [''] * y
result = []

# 가로
for _ in range(x):
    s = stdin.readline().rstrip()
    tmp = [i for i in list(s.split('#')) if len(i) > 1]
    result += tmp
    for i in range(y):
        word[i] += s[i]

# 세로
for t in word:
    tmp1 = [i for i in list(t.split('#')) if len(i) > 1]
    result += tmp1

result.sort()
print(result[0])