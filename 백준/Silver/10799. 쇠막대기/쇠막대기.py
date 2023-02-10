arr = input()
arr = arr.replace('()', '-')
bar = 0
n = 0

for i in arr:
    if i == '(':
        n += 1
    elif i == '-':
        bar += n
    else:
        n -= 1
        bar += 1

print(bar)