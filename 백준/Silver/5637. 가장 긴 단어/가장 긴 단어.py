from sys import stdin

result = ''
chk = 0
f = "1234567890.,()\""

while chk == 0:
    s = stdin.readline().rstrip()
    for c in f:
        s = s.replace(c, "")

    tmp = list(s.split())
    if 'E-N-D' in tmp:
        chk = 1
        tmp.pop()

    tmp.sort(key=lambda x: len(x), reverse=True)

    if len(tmp) > 0:
        if len(tmp[0]) > len(result):
            result = tmp[0]

print(result.lower())