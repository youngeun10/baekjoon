from sys import stdin

n = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

s, e = map(int, stdin.readline().split())
result = []
for i in range(s, e+1):
    if i < 10:
        result.append((i, n[i]))
    else:
        tmp = n[i//10] + n[i%10]
        result.append((i, tmp))

result.sort(key=lambda x: x[1])

for i in range(e-s+1):
    if i % 10 == 9:
        print(result[i][0])
    else:
        print(result[i][0], end=' ')