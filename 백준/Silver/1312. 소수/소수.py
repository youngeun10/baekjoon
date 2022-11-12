from sys import stdin

a, b, v = map(int, stdin.readline().split())

for i in range(v):
    a = (a % b) * 10
    result = a // b

print(result)