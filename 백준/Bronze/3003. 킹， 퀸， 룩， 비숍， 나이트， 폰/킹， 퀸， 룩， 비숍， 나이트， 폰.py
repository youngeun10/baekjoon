c = [1, 1, 2, 2, 2, 8]
s = list(map(int, input().split()))
print(*[c[i] - s [i] for i in range(len(c))])