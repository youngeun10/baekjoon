from sys import stdin

for _ in range(int(stdin.readline())):
    tmp1 = list(stdin.readline().rstrip().split(','))
    tmp2 = list(stdin.readline().rstrip().split('|'))
    result = []
    arr = {}
    for i in tmp1:
        a, b = i.split(':')
        arr[a] = int(b)

    for j in tmp2:
        t = list(j.split('&'))
        s = arr[t[0]]
        for x in range(1, len(t)):
            if s < arr[t[x]]:
                s = arr[t[x]]
        result.append(s)
    print(min(result))