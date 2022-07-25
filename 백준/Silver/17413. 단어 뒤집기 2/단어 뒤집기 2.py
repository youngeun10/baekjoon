from sys import stdin

def listToStr(a):
    r = ''
    for i in a:
        r += i
    return r

arr = stdin.readline()
s = []
result = []
chk = 0
for i in range(len(arr)):

    if arr[i] == '<':
        chk = 1
        if s:
            s.reverse()
            tmp = listToStr(s)
            result.append(tmp)
            s = []
        s.append('<')
    elif arr[i] == '>':
        chk = 0
        s.append('>')
        tmp = listToStr(s)
        result.append(tmp)
        s = []
    elif arr[i] == ' ' or arr[i] == '\n':
        if chk == 1:
            s.append(arr[i])
        else:
            s.reverse()
            tmp = listToStr(s)
            result.append(tmp)
            s = []

            if arr[i] == ' ':
                result.append(' ')
    else:
        s.append(arr[i])

print(listToStr(result))