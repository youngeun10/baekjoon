from sys import stdin

result = []
for _ in range(int(stdin.readline())):
    n = {}
    arr = list(map(int, stdin.readline().split()))

    for i in arr:
        if i not in n:
            n[i] = 1
        else:
            n[i] += 1
    
    if len(n) == 3:
        result.append(max(n.keys()) * 100)
    elif len(n) == 2:
        t = [k for k, v in n.items() if v == 2]
        result.append(1000 + (t[0]*100))
    else:
        result.append(10000 + (arr[0]*1000))

print(max(result))