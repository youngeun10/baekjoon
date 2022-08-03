def change(arr, c, d):
    z = len(arr) - 1
    cnt = 0
    while c in s:
        if c * z in s:
            cnt += arr.count(c * z)
            arr = arr.replace(c * z, d * z)
            z -= 1
        else:
            z -= 1

        if z < 1:
            break
    return cnt

s = input()
print(min(change(s, '0', '1'), change(s, '1', '0')))