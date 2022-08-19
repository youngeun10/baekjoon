p1, p2, p3, x1, x2, x3 = map(int, input().split())
m = min(x1, x2, x3)

for i in range(1, p1*p2*p3):
    if (i % p1 == x1) and (i % p2 == x2) and (i % p3 == x3):
        print(i)
        quit()
print(-1)