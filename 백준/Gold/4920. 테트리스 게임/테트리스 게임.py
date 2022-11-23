def a(n, a):
    for i in range(n):
        for j in range(n - 3):
            if i == 0 and j == 0:
                m = a[i][j] + a[i][j + 1] + a[i][j + 2] + a[i][j + 3]
            else:
                hap = a[i][j] + a[i][j + 1] + a[i][j + 2] + a[i][j + 3]
                if hap > m:
                    m = hap

    for i in range(n-3):
        for j in range(n):
            hap = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+3][j]
            if hap > m:
                m = hap

    for i in range(n - 1):
        for j in range(n - 1):
            hap = a[i][j] + a[i][j + 1] + a[i + 1][j] + a[i + 1][j + 1]
            if hap > m:
                m = hap

    for i in range(n - 1):
        for j in range(n - 2):
            hap2 = a[i][j] + a[i][j + 1] + a[i + 1][j + 1] + a[i + 1][j + 2]
            hap31 = a[i][j] + a[i][j + 1] + a[i][j + 2] + a[i + 1][j + 2]
            hap32 = a[i][j] + a[i + 1][j] + a[i + 1][j + 1] + a[i + 1][j + 2]
            hap41 = a[i][j] + a[i][j + 1] + a[i][j + 2] + a[i + 1][j + 1]
            hap42 = a[i][j + 1] + a[i + 1][j] + a[i + 1][j + 1] + a[i + 1][j + 2]

            if max(hap2, hap31, hap32, hap41, hap42) > m:
                m = max(hap2, hap31, hap32, hap41, hap42)

    for i in range(n - 2):
        for j in range(n - 1):
            hap2 = a[i][j + 1] + a[i + 1][j] + a[i + 1][j + 1] + a[i + 2][j]
            hap31 = a[i][j + 1] + a[i + 1][j + 1] + a[i + 2][j] + a[i + 2][j + 1]
            hap32 = a[i][j] + a[i][j + 1] + a[i + 1][j] + a[i + 2][j]
            hap41 = a[i][j] + a[i + 1][j] + a[i + 1][j + 1] + a[i + 2][j]
            hap42 = a[i][j + 1] + a[i + 1][j] + a[i + 1][j + 1] + a[i + 2][j + 1]

            if max(hap2, hap31, hap32, hap41, hap42) > m:
                m = max(hap2, hap31, hap32, hap41, hap42)
    return m

t = 1

while True:
    num = int(input())

    if num == 0:
        break

    arr = []

    for i in range(num):
        arr.append(list(map(int, input().split())))

    print(f'{t}. {a(num, arr)}')
    t += 1

