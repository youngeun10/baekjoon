from sys import stdin

n = int(stdin.readline().rstrip())
for i in range(n):
    arr = list(stdin.readline().rstrip().split())
    print(f"Case #{i+1}: ", end='')
    for j in arr[::-1]:
        print(j, end=' ')
    print()