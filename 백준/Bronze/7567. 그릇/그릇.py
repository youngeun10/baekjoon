from sys import stdin

a = stdin.readline().rstrip()
result = 10

for i in range(1, len(a)):
    if a[i] != a[i-1]:
        result += 10
    else:
        result += 5
    
print(result)