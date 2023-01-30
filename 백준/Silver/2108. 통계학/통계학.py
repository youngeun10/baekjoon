from sys import stdin

n = int(stdin.readline())
arr = [0] * n
d = {}      # 숫자별 count
dcnt = {}
sum = 0

for i in range(n):
    arr[i] = int(stdin.readline())
    sum += arr[i]

    if arr[i] not in d:
        d[arr[i]] = 1
        if 1 not in dcnt:
            dcnt[1] = [arr[i]]
        else:
            dcnt[1].append(arr[i])
    else:
        d[arr[i]] += 1
        if d[arr[i]] not in dcnt:
            dcnt[d[arr[i]]] = [arr[i]]
        else:
            dcnt[d[arr[i]]].append(arr[i])

arr.sort()
tmp = dcnt[max(d.values())]
tmp.sort()


print(round(sum/n))
print(arr[n//2])
print(tmp[1]) if len(tmp) > 1 else print(tmp[0])
print(arr[-1]-arr[0])